from student import Student
from group import Group


# Тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(gr)
print()

# Перевірка порівняння
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
print("✓ Test 1 passed: Found Jobs")

assert gr.find_student('Jobs2') is None
print("✓ Test 2 passed: Jobs2 not found")

# Видалення студента
gr.delete_student('Taylor')
print("\nAfter deleting Taylor:")
print(gr)  # Only one student

print("\n All tests passed!")
