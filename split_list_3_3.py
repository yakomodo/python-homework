# Розділити один список на два списки

def split_list(lst):
    if len(lst) == 0:
        return [[], []]

    middle = len(lst) // 2
    if len(lst) % 2 != 0:
        middle += 1

    return [lst[:middle], lst[middle:]]


# Перевірка роботи (приклади з умови)
print(split_list([1, 2, 3, 4, 5, 6]))   # [[1, 2, 3], [4, 5, 6]]
print(split_list([1, 2, 3]))            # [[1, 2], [3]]
print(split_list([1, 2, 3, 4, 5]))       # [[1, 2, 3], [4, 5]]
print(split_list([1]))                   # [[1], []]
print(split_list([]))                    # [[], []]
