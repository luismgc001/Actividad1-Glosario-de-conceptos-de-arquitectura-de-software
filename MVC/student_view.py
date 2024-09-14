class StudentView:
    @staticmethod
    def show_students(students):
        if not students:
            print("No hay estudiantes.")
        else:
            print("Estudiantes:")
            for index, student in enumerate(students, 1):
                print(f"{index}. {student['name']} - Nota: {student['grade']}")

    @staticmethod
    def show_add_student(name, grade):
        print(f"Estudiante '{name}' con nota '{grade}' añadido.")

    @staticmethod
    def show_remove_student(student):
        if student:
            print(f"Estudiante '{student['name']}' eliminado.")
        else:
            print("Número de estudiante inválido.")
