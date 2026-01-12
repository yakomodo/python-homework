# Найпростіший калькулятор

a = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

if operation == "+":
    result = a + b
    print("Результат:", result)

elif operation == "-":
    result = a - b
    print("Результат:", result)

elif operation == "*":
    result = a * b
    print("Результат:", result)

elif operation == "/":
    if b == 0:
        print("Помилка: ділити на нуль не можна")
    else:
        result = a / b
        print("Результат:", result)

else:
    print("Помилка: невідома операція")
