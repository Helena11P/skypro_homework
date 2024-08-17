def bank(x, y):
    for cont in range(1, y+1):
        cont = x + (x * 0.1)
        x = cont
    print("Размер вклада через", y, "лет:", x)


x = int(input("Размер вклада: "))
y = int(input("Количество лет: "))

bank(x, y)
