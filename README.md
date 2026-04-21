# MFAU Simulator (Atomic Flow Unified Model)

Este repositorio contiene el motor de física y el simulador visual para la **Teoría del Flujo Atómico Unificado (MFAU)**, desarrollada por Eliezer Siqueira Salles.

## 🚀 Concepto de la Simulación
A diferencia de los simuladores de gravedad convencionales basados en fuerzas a distancia (Newton), este software modela la gravedad como una **interacción cinemática con el medio**.

### Características Clave:
*   **Flujo Espacial ($v_f$):** El espacio se mueve radialmente hacia los átomos a $v = \sqrt{2GM/r}$.
*   **Acoplamiento Diferenciado ($\eta$):** 
    *   Materia bariónica: $\eta = 0.5$ (Inercia).
    *   Luz (Fotones): $\eta = 1.0$ (Acoplamiento total).
*   **Dilatación Temporal de Pitágoras:** El tiempo local se calcula mediante la hipotenusa de arrastre del flujo, recuperando la métrica de Schwarzschild sin geometría curva.
*   **Redshift Gravitacional:** Visualización del cambio de frecuencia lumínica según la velocidad del flujo local.

## 🛠️ Requisitos
*   Python 3.x
*   Pygame (`pip install pygame`)

## 📖 Referencias
Este código es el soporte numérico del artículo:
**"Unificación Cinemática de la Gravedad y la Mecánica Cuántica mediante el Modelo de Flujo Atómico (MFAU)"** publicado en Zenodo https://doi.org/10.5281/zenodo.19672659 
