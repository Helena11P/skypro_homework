def is_year_leap(year):
    if (year % 4 == 0):
        return True
    else:
        return False


year = int(input("Введите год: "))
y = is_year_leap(year)
print("Год", year, ":", y)
