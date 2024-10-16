def generate_random_numbers(size, lower_bound, upper_bound):
    seed = 123456
    random_numbers = []

    for _ in range(size):
        seed = (1664525 * seed + 1013904223) % (2**32)
        random_numbers.append(seed % (upper_bound + 1))

    return random_numbers

def find_multiples():
    numbers = generate_random_numbers(10, 0, 200)
    
    x = int(input("Введите число X: "))
    
    multiples = list(filter(lambda n: n % x == 0, numbers))
    
    print(f"Сгенерированные числа: {numbers}")
    print(f"Числа, кратные {x}: {multiples}")

find_multiples()
