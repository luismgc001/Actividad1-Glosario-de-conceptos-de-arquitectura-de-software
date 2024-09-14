class StudentModel:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        self.students.append({"name": name, "grade": grade})

    def get_students(self):
        return self.students

    def remove_student(self, student_number):
        try:
            return self.students.pop(student_number - 1)
        except IndexError:
            return None
