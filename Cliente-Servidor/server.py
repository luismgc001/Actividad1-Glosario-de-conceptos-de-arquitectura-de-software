import socket
import threading

tasks = []

def handle_client(client_socket):
    global tasks
    while True:
        # Recibir la solicitud del cliente
        request = client_socket.recv(1024).decode()
        
        if request.startswith('ADD'):
            task = request[4:]
            tasks.append(task)
            client_socket.send(f"Tarea '{task}' añadida.".encode())
        elif request == 'VIEW':
            if not tasks:
                client_socket.send("No hay tareas.".encode())
            else:
                response = "Tareas:\n" + "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])
                client_socket.send(response.encode())
        elif request.startswith('REMOVE'):
            try:
                task_number = int(request[7:]) - 1
                removed_task = tasks.pop(task_number)
                client_socket.send(f"Tarea '{removed_task}' eliminada.".encode())
            except (IndexError, ValueError):
                client_socket.send("Número de tarea inválido.".encode())
        elif request == 'EXIT':
            client_socket.send("Desconectando...".encode())
            break

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Servidor escuchando en el puerto 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexión aceptada desde {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
