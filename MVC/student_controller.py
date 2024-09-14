from student_model import StudentModel
from student_view import StudentView

class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_student(self, name, grade):
        self.model.add_student(name, grade)
        self.view.show_add_student(name, grade)

    def view_students(self):
        students = self.model.get_students()
        self.view.show_students(students)

    def remove_student(self, student_number):
        removed_student = self.model.remove_student(student_number)
        self.view.show_remove_student(removed_student)

def main():
    model = StudentModel()
    view = StudentView()
    controller = StudentController(model, view)
    
    while True:
        print("\n1. Añadir estudiante")
        print("2. Ver estudiantes")
        print("3. Eliminar estudiante")
        print("4. Salir")

        choice = input("Elige una opción: ")

        if choice == '1':
            name = input("Introduce el nombre del estudiante: ")
            grade = input("Introduce la nota del estudiante: ")
            controller.add_student(name, grade)
        elif choice == '2':
            controller.view_students()
        elif choice == '3':
            student_number = int(input("Introduce el número del estudiante a eliminar: "))
            controller.remove_student(student_number)
        elif choice == '4':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
