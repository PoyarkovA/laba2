def calc():
    b_d = int(input("Введите день рождения: "))
    b_m = int(input("Введите месяц рождения: "))
    b_y = int(input("Введите год рождения: "))

    t_d = int(input("Введите сегодняшний день: "))
    t_m = int(input("Введите сегодняшний месяц: "))
    t_y = int(input("Введите сегодняшний год: "))

    age = t_y - b_y - ((t_m, t_d) < (b_m, b_d))
    print(f"Ваш возраст: {age} лет")

calc()
