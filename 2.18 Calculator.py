a = float(input())
b = float(input())
operation = input()

match operation:
    case "+":
        out = a + b
    case "-":
        out = a - b
    case "/":
        if b != 0:
            out = a / b
        else:
            out = "Division by 0!"
    case "*":
        out = a * b
    case "mod":
        if b != 0:
            out = a % b
        else:
            out = "Division by 0!"
    case "div":
        if b != 0:
            out = a // b
        else:
            out = "Division by 0!"
    case "pow":
        out = a ** b

print(out)
