import string

def letter_range(user_input):
    start_letter, end_letter = user_input.split('-')
    
    start_index = string.ascii_letters.index(start_letter)
    end_index = string.ascii_letters.index(end_letter)
    
    result = string.ascii_letters[start_index:end_index + 1]
    
    return result

user_input = input("Введіть діапазон (наприклад, a-c): ")
print(letter_range(user_input))
