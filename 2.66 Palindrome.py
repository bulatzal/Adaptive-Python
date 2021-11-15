string = input()
k = 0

for i in range(len(string)):
    if string[i] == string[len(string) - i - 1]:
        k += 1

if k == len(string):
    print("yes")
else:
    print("no")
