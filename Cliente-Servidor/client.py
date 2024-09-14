import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))

    while True:
        print("\n1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            task = input("Introduce la tarea: ")
            client.send(f'ADD {task}'.encode())
        elif choice == '2':
            client.send('VIEW'.encode())
        elif choice == '3':
            task_number = input("Introduce el número de tarea a eliminar: ")
            client.send(f'REMOVE {task_number}'.encode())
        elif choice == '4':
            client.send('EXIT'.encode())
            break
        else:
            print("Opción no válida.")
            continue

        # Recibir respuesta del servidor
        response = client.recv(1024).decode()
        print(f"Servidor: {response}")

    client.close()

if __name__ == "__main__":
    main()
