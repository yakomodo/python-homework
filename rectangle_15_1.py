class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        """Порівняння прямокутників за площею"""
        return self.get_square() == other.get_square()

    def __add__(self, other):
        """Складання прямокутників (сума площ)"""
        new_area = self.get_square() + other.get_square()
        # Створюємо новий прямокутник зі сторонами 1 × площа
        return Rectangle(1, new_area)

    def __mul__(self, n):
        """Множення прямокутника на число"""
        new_area = self.get_square() * n
        # Створюємо новий прямокутник зі сторонами 1 × нова_площа
        return Rectangle(1, new_area)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


# Тести
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print(' All tests passed!')