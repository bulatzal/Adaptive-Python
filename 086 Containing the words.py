words = [str(n) for n in input().split()]

wordsLength = []
wordsAmount = []
for i in words:
    wordsLength.append(len(i))
length = list(set(wordsLength))
for i in length:
    wordsAmount.append(wordsLength.count(i))
for i in range(len(length)):
    print(length[i], ":", wordsAmount[i])
