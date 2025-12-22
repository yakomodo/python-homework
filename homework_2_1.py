### Завдання 1.
number = int(input("Введіть число: "))
print("Квадрат числа:", number ** 2)

### Завдання 2.
numbers = input("Введіть три числа: ").split(", ")
numbers = int(numbers[0]), int(numbers[1]), int(numbers[2])
average = sum(numbers) / 3
print("Середнє:", average)

### Завдання 3.
mins = int(input("Введіть кількість хвилин: "))
hrs = mins // 60
mins_left = mins % 60
print(hrs, "години", mins_left, "хвилини")

### Завдання 4.
price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
final_price = price * (100 - discount)/100 
print("Ціна зі знижкою:", final_price)

### Завдання 5.
num = int(input("Введіть число: "))
last_num = num % 10
print("Остання цифра:", last_num)

### Завдання 6.
length = int(input("Введіть довжину: "))
width = int(input("Введіть ширину: "))
perimeter = 2 * (length + width) 
print("Периметр:", perimeter)

### Завдання 7.
four_dit = int(input("Введіть 4-значне число: "))
print(four_dit // 1000)
print((four_dit // 100) % 10)
print((four_dit // 10) % 10)
print(four_dit % 10)