import pygame
import math
import random

# --- CONFIGURACIÓN MFAU ---
WIDTH, HEIGHT = 900, 900
FPS = 60
C = 40.0                # Velocidad de la luz constante en el medio
ETA_MATTER = 0.5        # Acoplamiento de la materia (inercia)
ETA_LIGHT = 1.0         # Acoplamiento de la luz (1:1)
G_INTENSITY = 4000      # Intensidad de succión (Phi * M)

# --- COLORES ---
COLOR_SPACE = (5, 5, 20)
COLOR_MASS = (0, 100, 255)
COLOR_METEOR = (255, 0, 255)
COLOR_LIGHT = (255, 255, 100)

class Meteor:
    def __init__(self, pos, vel):
        self.pos = list(pos)
        self.vel = list(vel)
        self.path = []

class LightRay:
    def __init__(self, pos, angle):
        self.pos = list(pos)
        self.angle = angle

# --- MOTOR DE FÍSICA MFAU ---
def get_flow_data(x, y):
    dx = center_pos[0] - x
    dy = center_pos[1] - y
    r = math.hypot(dx, dy)
    
    if r < 10: return 0, 0, 0, 1.0
    
    # 1. Velocidad del flujo (v_f = sqrt(2GM/r))
    v_f_mag = math.sqrt(2 * G_INTENSITY / r)
    v_f_x = (dx / r) * v_f_mag
    v_f_y = (dy / r) * v_f_mag
    
    # 2. Aceleración (g = eta * v_f^2 / 2r)
    # El flujo acelera hacia el centro
    g_base = (v_f_mag**2) / (2 * r)
    
    # 3. Distorsión temporal (T = T0 * sqrt(1 - vf^2/c^2))
    # Basado en el Triángulo de Pitágoras
    time_factor = math.sqrt(max(0, 1 - (v_f_mag**2 / C**2)))
    
    return v_f_x, v_f_y, g_base, time_factor

# --- INICIALIZACIÓN ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MFAU - Simulador de Flujo Atómico Unificado")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 16)

center_pos = [WIDTH//2, HEIGHT//2]
star_pos = [WIDTH//4, HEIGHT//4]
meteors = []
lights = []
dragging_star = False
dragging_launch = False
launch_start = [0,0]

running = True
while running:
    screen.fill(COLOR_SPACE)
    mx, my = pygame.mouse.get_pos()

    # --- EVENTOS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if math.hypot(mx - star_pos[0], my - star_pos[1]) < 20:
                dragging_star = True
            else:
                dragging_launch = True
                launch_start = [mx, my]
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging_star: dragging_star = False
            if dragging_launch:
                dx = (launch_start[0] - mx) * 0.05
                dy = (launch_start[1] - my) * 0.05
                meteors.append(Meteor(launch_start, [dx, dy]))
                dragging_launch = False

    if dragging_star: star_pos = [mx, my]

    # --- DIBUJAR MALLA Y FLUJO ---
    for x in range(0, WIDTH, 50):
        for y in range(0, HEIGHT, 50):
            vx, vy, g, t = get_flow_data(x, y)
            # Dibujar el vector del río de espacio
            end_x = x + vx * 2
            end_y = y + vy * 2
            pygame.draw.line(screen, (0, 40, 80), (x, y), (end_x, end_y), 1)

    # --- GENERAR LUZ ---
    if pygame.time.get_ticks() % 4 == 0:
        angle = random.uniform(0, 2*math.pi)
        lights.append(LightRay(star_pos, angle))

    # --- ACTUALIZAR LUZ (ETA = 1.0) ---
    for l in lights[:]:
        vfx, vfy, g, t = get_flow_data(l.pos[0], l.pos[1])
        # Luz = Velocidad Propia (C) + Flujo (ETA 1.0)
        vx = math.cos(l.angle) * C + vfx * ETA_LIGHT
        vy = math.sin(l.angle) * C + vfy * ETA_LIGHT
        
        # En la MFAU la luz se curva porque el medio la arrastra
        l.pos[0] += vx * 0.5
        l.pos[1] += vy * 0.5
        l.angle = math.atan2(vy, vx)

        if math.hypot(l.pos[0]-center_pos[0], l.pos[1]-center_pos[1]) < 15 or not (0 < l.pos[0] < WIDTH):
            lights.remove(l)
        else:
            # Color por distorsión temporal (Redshift)
            color_val = int(255 * t)
            pygame.draw.circle(screen, (255, color_val, color_val), (int(l.pos[0]), int(l.pos[1])), 1)

    # --- ACTUALIZAR METEORITOS (ETA = 0.5) ---
    for m in meteors[:]:
        vfx, vfy, g, t = get_flow_data(m.pos[0], m.pos[1])
        
        # Aceleración g = 0.5 * v_f^2 / 2r
        dist = math.hypot(center_pos[0]-m.pos[0], center_pos[1]-m.pos[1])
        if dist > 10:
            ax = (center_pos[0] - m.pos[0]) / dist * g * ETA_MATTER
            ay = (center_pos[1] - m.pos[1]) / dist * g * ETA_MATTER
            m.vel[0] += ax
            m.vel[1] += ay

        m.pos[0] += m.vel[0]
        m.pos[1] += m.vel[1]
        m.path.append(list(m.pos))
        if len(m.path) > 40: m.path.pop(0)

        if len(m.path) > 2:
            pygame.draw.lines(screen, COLOR_METEOR, False, m.path, 2)
        
        if dist < 15 or not (0 < m.pos[0] < WIDTH):
            meteors.remove(m)

    # --- UI Y INFO ---
    _, _, _, mouse_t = get_flow_data(mx, my)
    info = font.render(f"Tiempo Local: {mouse_t:.6f} t0 | Flujo: {math.sqrt(G_INTENSITY/max(1,math.hypot(mx-center_pos[0], my-center_pos[1]))):.2f} v", True, (255, 255, 255))
    screen.blit(info, (10, 10))

    # --- DIBUJAR MASAS ---
    pygame.draw.circle(screen, COLOR_MASS, center_pos, 15) # Sumidero
    pygame.draw.circle(screen, (255, 255, 255), star_pos, 8) # Estrella
    if dragging_launch:
        pygame.draw.line(screen, (255, 255, 255), launch_start, (mx, my), 1)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
