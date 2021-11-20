x = int(input())
move = "move"

match x:
    case 1:
        print(move, "up")
    case 2:
        print(move, "down")
    case 3:
        print(move, "left")
    case 4:
        print(move, "right")
    case 0:
        print("do not", move)
    case _:
        print("error!")
