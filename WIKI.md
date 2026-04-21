# 📚 Documentación del Motor de Física MFAU

Este simulador no utiliza las ecuaciones de fuerza de Newton $F = G \frac{m_1 m_2}{r^2}$, sino que implementa una **cinemática de fluidos** basada en el **Modelo de Flujo Atómico Unificado**.

## 1. El Motor de Flujo ($v_f$)
El núcleo de la simulación es la función `get_flow_data`. Representa el espacio moviéndose radialmente hacia la masa azul.

$$v_{flujo} = \sqrt{\frac{2 \Phi M}{r}}$$

Las líneas azules en el fondo del simulador muestran la dirección y magnitud de este "viento" espacial.

## 2. Acoplamiento Diferenciado ($\eta$)
El simulador demuestra visualmente la tesis central del MFAU sobre la deflexión lumínica:

*   **Meteoritos ($\eta = 0.5$):** Tienen inercia. Su aceleración es la mitad de la aceleración del flujo. Verás que describen órbitas más abiertas.
*   **Luz ($\eta = 1.0$):** Se acopla totalmente al medio. Verás que los rayos amarillos se curvan el **doble** que la materia al pasar por el mismo punto, validando mecánicamente la predicción de 1.75" de arco.

## 3. El Triángulo de Pitágoras y el Tiempo
En la esquina superior izquierda verás el valor del **Tiempo Local**. Se calcula en tiempo real para la posición de tu ratón usando la hipotenusa de arrastre:

$$T = \sqrt{1 - \frac{v_{flujo}^2}{c^2}}$$

A medida que acercas el ratón a la masa central (donde el flujo es más rápido), verás cómo el tiempo se acerca a $0$.

## 4. Redshift Visual
Los fotones (rayos de luz) cambian de color dinámicamente:
*   **Blanco/Amarillo:** En zonas de flujo lento (tiempo rápido).
*   **Rojo:** Al entrar en zonas de flujo rápido (tiempo lento). 

## 5. Sincronización y Velocidad Límite
Si lanzas un meteorito con el "tirachinas" a una velocidad superior al flujo, observarás que el objeto **no acelera más**. En la MFAU, un objeto no puede ser impulsado por la gravedad más allá de la velocidad del propio río de espacio que lo transporta.

---

### Controles del Simulador:
*   **Clic Izquierdo (Arrastrar):** Mueve la estrella emisora de luz.
*   **Clic Derecho (Arrastrar):** Lanza meteoritos (tirachinas).
*   **Movimiento del Ratón:** Muestra la distorsión temporal local.
