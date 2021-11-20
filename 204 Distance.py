from math import sqrt


def distance(_x1, _y1, _x2, _y2):
    dist = sqrt((_x2 - _x1) ** 2 + (_y2 - _y1) ** 2)
    dist = round(dist, 5)
    return dist


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

out = distance(x1, y1, x2, y2)
print(out)
