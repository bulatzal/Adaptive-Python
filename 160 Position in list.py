numbers = list(map(int, input().split()))
x = int(input())

output = []

for i in range(len(numbers)):
    if numbers[i] == x:
        output.append(i)

print(*output, sep=" ") if output else print("Missing")
