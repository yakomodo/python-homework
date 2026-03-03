from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        """Додає студента до групи"""
        if len(self.group) >= 10:
            raise ValueError("Група не може містити більше 10 студентів")
        self.group.add(student)

    def delete_student(self, last_name):
        """Видаляє студента за прізвищем"""
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        """Шукає студента за прізвищем"""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        """Повертає інформацію про групу"""
        all_students = '\n'.join(str(student) for student in self.group)
        return f"Group {self.number}:\n{all_students}"
