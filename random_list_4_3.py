import random

length = random.randint(3, 10)
original_list = [random.randint(1, 10) for _ in range(length)]

# 2
result_list = [original_list[0], original_list[2], original_list[-2]]

print(f"Оригінальний список: {original_list}")
print(f"Результат: {result_list}")