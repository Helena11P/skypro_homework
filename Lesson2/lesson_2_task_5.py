def month_for_season(m):
    if (m == 1) or (m == 2) or (m == 12):
        print("Зима")
    elif (m == 3) or (m == 4) or (m == 5):
        print("Весна")
    elif (m == 6) or (m == 7) or (m == 8):
        print("Лето")
    else:
        print("Осень")


m = int(input("Введите номер месяца: "))

month_for_season(m)
