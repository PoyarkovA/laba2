def get_number():
    for number in range(30):
        if number % 2 != 0: 
            yield number

def print_selected_numbers():
    numbers = list(get_number())
    
    if len(numbers) > 0:
        print(f"Первое нечетное число: {numbers[0]}")
    if len(numbers) > 4:
        print(f"Пятое нечетное число: {numbers[4]}")
    if len(numbers) > 0:
        print(f"Последнее нечетное число: {numbers[-1]}")

print_selected_numbers()
