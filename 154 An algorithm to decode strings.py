string = input()

number = ''
decodedString = ''

for i in range(len(string)):
    if string[i].isdigit():
        number += string[i]
    else:
        if number == '':
            number = '1'
        decodedString += int(number) * string[i]
        number = ''

print(decodedString)
