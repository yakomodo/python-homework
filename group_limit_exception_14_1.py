class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}, Record book: {self.record_book}"


# Власний виняток
class GroupLimitError(Exception):
    """Виняток для перевищення ліміту студентів у групі"""
    def __init__(self, message="Не можна додати більше 10 студентів до групи"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\nStudents: {len(self.group)}\n{all_students}'


# Тест
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')

# Додаємо перших двох студентів
gr.add_student(st1)
gr.add_student(st2)

# Додаємо ще 8 студентів (всього стане 10)
for i in range(3, 11):
    student = Student('Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN{100 + i}')
    gr.add_student(student)

print(gr)
print(f"\nВ групі {len(gr.group)} студентів")

# Спроба додати 11-го студента
try:
    st11 = Student('Male', 25, 'Extra', 'Student', 'AN999')
    gr.add_student(st11)
except GroupLimitError as e:
    print(f"\n Помилка: {e}")

print(f"\nПісля спроби додавання: {len(gr.group)} студентів")
print('\n OK')