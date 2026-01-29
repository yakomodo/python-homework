def seconds_to_time(seconds):
    SECONDS_IN_DAY = 24 * 60 * 60  
    SECONDS_IN_HOUR = 60 * 60 
    SECONDS_IN_MINUTE = 60
    
    # дні
    days = seconds // SECONDS_IN_DAY
    seconds = seconds % SECONDS_IN_DAY
    
    # години
    hours = seconds // SECONDS_IN_HOUR
    seconds = seconds % SECONDS_IN_HOUR
    
    # хвилини
    minutes = seconds // SECONDS_IN_MINUTE
    seconds = seconds % SECONDS_IN_MINUTE
    
    # відмінювання
    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
        day_word = "дні"
    else:
        day_word = "днів"
    
    # нулі
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    
    return f"{days} {day_word}, {time_str}"

user_input = int(input("Введіть кількість секунд: "))
print(seconds_to_time(user_input))