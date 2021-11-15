N = int(input())

if N < 100 or N > 999:
    print("Enter a three-digit int")
else:
    total = (N // 100) + (N % 10) + (N % 100 // 10)
    print(total)
