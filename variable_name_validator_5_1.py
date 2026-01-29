import string
import keyword

def is_valid_variable_name(name):
    # порожній рядок
    if not name:
        return False
    # не більше одного підкреслення
    if name.count('_') > 1:
        return False
    # не може бути зареєстрованим словом
    if name in keyword.kwlist:
        return False
    # не може починатися з цифри
    if name[0].isdigit():
        return False
    # не може містити великі літери
    if any(char.isupper() for char in name):
        return False
    # не може містити пробіли або знаки пунктуації (окрім '_')
    for char in name:
        if char in string.punctuation and char != '_':
            return False
        if char == ' ':
            return False 
    return True

user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(user_input))