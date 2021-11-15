V = int(input())
T = int(input())

if (V > 1000) or (V < -1000) or (T < 0) or (T > 1000):
    print("Enter V [-1000;1000], T [0;1000]")
elif V > 0:
    s = (V * T) % 109
elif V < 0:
    s = (109 + V * T) % 109
else:
    s = 0

print(s)
