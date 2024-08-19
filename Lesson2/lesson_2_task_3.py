import math


def square(a):
    s = a * a
    return math.ceil(s)


s = square(6.5)

print("Площадь квадрата:", s)
