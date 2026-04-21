📚 Documentación del Motor de Física MFAU
Este simulador no utiliza las ecuaciones de fuerza de Newton (


), sino que implementa una cinemática de fluidos basada en el Modelo de Flujo Atómico Unificado.
1. El Motor de Flujo (
)
El núcleo de la simulación es la función get_flow_data. Representa el espacio moviéndose radialmente hacia la masa azul.
Fórmula: 

Representación: Las líneas azules en el fondo del simulador muestran la dirección y magnitud de este "viento" espacial.
2. Acoplamiento Diferenciado (
)
El simulador demuestra visualmente la tesis central del MFAU sobre la deflexión lumínica:
Meteoritos (

): Tienen inercia. Su aceleración es la mitad de la aceleración del flujo. Verás que describen órbitas más abiertas.
Luz (

): Se acopla totalmente al medio. Verás que los rayos amarillos se curvan el doble que la materia al pasar por el mismo punto, validando mecánicamente la predicción de 1.75" de arco.
3. El Triángulo de Pitágoras y el Tiempo
En la esquina superior izquierda verás el valor del Tiempo Local.
Lógica: Se calcula en tiempo real para la posición de tu ratón usando la hipotenusa de arrastre: 

.
Observación: A medida que acercas el ratón a la masa central (donde el flujo es más rápido), verás cómo el tiempo se acerca a 
.
4. Redshift Visual
Los fotones (rayos de luz) cambian de color dinámicamente:
Blanco/Amarillo: En zonas de flujo lento (tiempo rápido).
Rojo: Al entrar en zonas de flujo rápido (tiempo lento).
Esto visualiza cómo la frecuencia de la luz se estira para ajustarse al ritmo temporal del medio.
5. Sincronización y Velocidad Límite
Si lanzas un meteorito con el "tirachinas" (clic derecho y arrastrar) a una velocidad superior al flujo, observarás que el objeto no acelera más. En la MFAU, un objeto no puede ser impulsado por la gravedad más allá de la velocidad del propio río de espacio que lo transporta.
Controles del Simulador:
Clic Izquierdo (Arrastrar): Mueve la estrella emisora de luz.
Clic Derecho (Arrastrar): Lanza meteoritos (tirachinas).
Movimiento del Ratón: Muestra la distorsión temporal local en esa coordenada.
