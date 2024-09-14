
# Ejemplos de Patrones de Arquitectura de Software

Este repositorio contiene ejemplos prácticos de diferentes patrones de arquitectura de software implementados en Python, ejecutables desde la ventana de comandos.

## 1. Patrón Monolítico
Toda la funcionalidad de la aplicación se encuentra en un solo proyecto o código base. Ideal para aplicaciones pequeñas o que no requieren alta escalabilidad.

- **Ejemplo**: Una aplicación de gestión de tareas sencilla desarrollada en Python con Flask, donde el frontend, la lógica de negocio y la base de datos están integrados en un solo proyecto.
- **Nuestro caso**: Haremos una pequeña aplicación que se ejecuta solo en la ventana de comandos.

**Carpeta**: `Tareas`

### Funcionamiento:
- **Añadir tarea**: Permite al usuario agregar una tarea a la lista.
- **Ver tareas**: Muestra las tareas que están almacenadas en memoria.
- **Eliminar tarea**: Elimina una tarea por su número en la lista.
- **Salir**: Finaliza el programa.

Esta aplicación gestiona tareas desde la terminal y almacena toda la información en memoria hasta que el programa se cierra.

---

## 2. Microservicios
La aplicación se divide en servicios pequeños e independientes que se comunican entre sí a través de APIs. Facilita la escalabilidad y el despliegue independiente.

- **Ejemplo**: Amazon utiliza microservicios para manejar distintos aspectos de su plataforma.
- **Nuestro caso**: Cada servicio se ejecuta como un script separado y se comunican usando mensajes a través de llamadas entre procesos.

**Carpeta**: `Microservicios`

### Funcionamiento:
- **Servicio de gestión de tareas (task_service.py)**: Permite agregar, ver y eliminar tareas. Cada vez que se añade o elimina una tarea, se ejecuta el servicio de notificaciones.
- **Servicio de notificaciones (notify_service.py)**: Imprime el mensaje de notificación que recibe como parámetro.

---

## 3. Patrón Cliente-Servidor
Un cliente solicita información o servicios a un servidor que los provee. Es una arquitectura clásica para aplicaciones distribuidas.

- **Ejemplo**: Una aplicación web donde el navegador solicita datos al servidor.
- **Nuestro caso**: Simularemos un servidor que gestiona tareas y un cliente que se conecta a él para enviar solicitudes y recibir respuestas.

**Carpeta**: `Cliente-Servidor`

### Funcionamiento:
- **Servidor (server.py)**: Maneja múltiples clientes y mantiene una lista de tareas en memoria. Escucha en el puerto 9999.
- **Cliente (client.py)**: Envía solicitudes para agregar, ver y eliminar tareas, y recibe las respuestas del servidor.

### Pasos para ejecutar:
1. Ejecuta el servidor (`server.py`).
2. Ejecuta el cliente (`client.py`) para interactuar con las tareas.

---

## 4. Patrón MVC (Modelo-Vista-Controlador)
Separa la lógica de la aplicación en tres componentes: el Modelo (datos), la Vista (interfaz de usuario) y el Controlador (maneja la interacción). Facilita la organización y mantenibilidad del código.

- **Ejemplo**: Aplicaciones desarrolladas con frameworks como Ruby on Rails.
- **Nuestro caso**: Un sistema de gestión de estudiantes que separa la lógica en tres componentes.

**Carpeta**: `MVC`

### Funcionamiento:
- **Modelo**: Gestiona una lista de estudiantes y permite agregar, ver y eliminar estudiantes.
- **Vista**: Muestra la lista de estudiantes y notifica las acciones.
- **Controlador**: Conecta la lógica del modelo con la vista y responde a las acciones del usuario.

### Pasos para ejecutar:
1. Crea los archivos `student_model.py`, `student_view.py` y `student_controller.py`.
2. Ejecuta `student_controller.py` desde la línea de comandos.

---

## 5. Event-Driven (Orientado a Eventos)
La comunicación entre componentes se basa en eventos, donde un componente emite eventos y otros reaccionan a ellos. Es útil para sistemas que requieren alta flexibilidad y respuesta en tiempo real.

- **Ejemplo**: Un sistema de notificaciones que emite un evento cuando se realiza una nueva acción.
- **Nuestro caso**: Un sistema simple de gestión de sensores donde los sensores envían eventos al detectar ciertos valores, y los listeners reaccionan a esos eventos.

**Carpeta**: `Event-Driven`

### Funcionamiento:
- **EventManager**: Permite que los listeners se suscriban a eventos y los notifica cuando un evento ocurre.
- **Sensor**: Genera un valor aleatorio y dispara un evento cuando dicho valor supera el umbral predefinido.
- **Listener**: Reacciona a eventos cuando se excede un umbral.

### Pasos para ejecutar:
1. Ejecutar el archivo `main.py` desde la línea de comandos.

---

Este repositorio está organizado para mostrar ejemplos claros de cómo implementar cada patrón de arquitectura en Python utilizando la línea de comandos.
