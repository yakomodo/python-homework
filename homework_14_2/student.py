class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):
        """Метод порівняння студентів"""
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        """Метод для можливості додавання в set"""
        return hash(str(self))
