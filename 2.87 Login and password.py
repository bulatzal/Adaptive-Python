login = 100500
password = 424242

login1, password1 = map(int, input().split(' '))
if (login1 == login) and (password1 == password):
    print("Login success")
elif login1 == login:
    print("Wrong password")
else:
    print("No user with login", login1, "found")
