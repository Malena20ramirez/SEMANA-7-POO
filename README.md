Estudiante:

 Malena Ramirez

## Descripción del Proyecto
Este repositorio contiene una versión mejorada, estructurada y modular del sistema "restaurante_app". El software simula la gestión básica de la administración interna de un restaurante, controlando tanto el catálogo de productos disponibles como los clientes registrados. 

A diferencia de las arquitecturas monolíticas, se aplica una separación estricta por capas a través de módulos interconectados.

## Estructura del Proyecto


```text
Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   └── cliente.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md
```


## Conceptos de POO Aplicados


*   **Encapsulamiento Avanzado (@property y @setter):** Implementado en la clase "Producto" para restringir el acceso directo a sus atributos críticos y validar en tiempo de asignación que las cadenas no estén vacías y que los precios ingresados sean estrictamente superiores a cero.

*   **Estructuras de Datos Eficientes (@dataclass):** Utilizado en la clase "Cliente" para simplificar la creación de objetos destinados exclusivamente al almacenamiento de datos.

*   **Arquitectura en Capas:** Distribución limpia del software dividida en "modelos" (estructuras lógicas de negocio), "servicios" (coordinadores y administradores de memoria) y un punto de control interactivo por terminal ("main.py").

## Reflexión 

La transición de probar software con datos "quemados" en el código hacia la captura dinámica mediante la entrada del usuario (input()) representa el verdadero puente entre la teoría académica y el desarrollo de software del mundo real.

Su importancia radica en dos pilares fundamentales: la adaptabilidad y la integridad. Un sistema real no puede predecir qué productos o clientes se van a registrar; por lo tanto, la creación dinámica dota al software de la flexibilidad para moldearse a las necesidades del usuario en tiempo real.

No obstante, abrir la puerta a datos externos introduce el riesgo del error humano. Aquí es donde la Programación Orientada a Objetos cobra su máximo sentido: la combinación de un menú interactivo con constructores y métodos @setter obliga al desarrollador a diseñar sistemas defensivos, donde la interfaz captura la información de manera flexible, pero las clases actúan como guardianes rigurosos que impiden que datos corruptos pongan en riesgo la estabilidad del negocio.