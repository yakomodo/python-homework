# Перемістити останній елемент списку на початок

def move_last_to_first(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]


# Перевірка роботи (приклади з умови)
print(move_last_to_first([12, 3, 4, 10]))        # [10, 12, 3, 4]
print(move_last_to_first([1]))                   # [1]
print(move_last_to_first([]))                    # []
print(move_last_to_first([12, 3, 4, 10, 8]))     # [8, 12, 3, 4, 10]
