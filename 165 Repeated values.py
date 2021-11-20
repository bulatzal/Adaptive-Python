M = list(map(int, input().split()))
M.sort()
M2 = []

for i in range(len(M)):
    if M.count(M[i]) > 1:
        M2 = M2 + [M[i]]

M2 = list(set(M2))

for i in range(len(M2)):
    print(M2[i], end=' ')
