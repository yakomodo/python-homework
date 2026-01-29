while True:
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        operation = input("Оберіть операцію (+, -, *, /): ")
        
        if operation == '+':
            print(f"Результат: {num1 + num2}")
        elif operation == '-':
            print(f"Результат: {num1 - num2}")
        elif operation == '*':
            print(f"Результат: {num1 * num2}")
        elif operation == '/':
            if num2 != 0:
                print(f"Результат: {num1 / num2}")
            else:
                print("Помилка: ділення на нуль!")
        else:
            print("Невідома операція!")
    
    except ValueError:
        print("Помилка: введіть коректне число!")
    
    # щоб продовжити
    if input("\nПродовжити? (yes/y): ").lower() not in ['yes', 'y']:
        print("До побачення!")
        break