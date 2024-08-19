def bank(x, y):
    for i in range(1, y+1):
        x += x * 0.1
    return x
    print("Размер вклада через", y, "лет:", x)


x = int(input("Размер вклада: "))
y = int(input("Количество лет: "))

print(f"Размер вклада через {y} лет: {bank(x, y)}")
