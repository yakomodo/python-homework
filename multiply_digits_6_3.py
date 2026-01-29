def multiply_digits(number):
    while number > 9:
        product = 1
       
        for digit in str(number):
            product *= int(digit)
        number = product
    
    return number

user_input = int(input("Введіть ціле число: "))
print(multiply_digits(user_input))