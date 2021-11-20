import math

figure = input()

match figure:
    case "rectangle":
        a = float(input())
        b = float(input())
        out = a * b
    case "circle":
        a = float(input())
        out = 3.14 * a * a
    case "triangle":
        a = float(input())
        b = float(input())
        c = float(input())
        p = (a + b + c) / 2
        out = math.sqrt(p * (p - a) * (p - b) * (p - c))
    case _:
        out = "Введите правильную фигуру"

print(out)
