def sum_even_indices(lst):
    if len(lst) == 0:
        return 0
    
    # lst[::2] -елементи з парними інд. (кожен 2гий, включаючи 0)
    sum_even = sum(lst[::2])
    result = sum_even * lst[-1]
    
    return result

# тест
print(sum_even_indices([0, 1, 7, 2, 4, 8]))  # 88
print(sum_even_indices([1, 3, 5]))  # 30
print(sum_even_indices([6]))  # 36
print(sum_even_indices([]))  # 0