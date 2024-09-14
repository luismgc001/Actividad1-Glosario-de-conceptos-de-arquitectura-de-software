import os

class TaskService:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarea '{task}' añadida.")
        os.system(f"python notify_service.py 'Tarea añadida: {task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No hay tareas.")
        else:
            print("Tareas:")
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        try:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Tarea '{removed_task}' eliminada.")
            os.system(f"python notify_service.py 'Tarea eliminada: {removed_task}'")
        except IndexError:
            print("Número de tarea inválido.")

def main():
    task_service = TaskService()
    
    while True:
        print("\n1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            task = input("Introduce la tarea: ")
            task_service.add_task(task)
        elif choice == '2':
            task_service.view_tasks()
        elif choice == '3':
            task_number = int(input("Introduce el número de tarea a eliminar: "))
            task_service.remove_task(task_number)
        elif choice == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
