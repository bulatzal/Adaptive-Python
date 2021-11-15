N = int(input())
hours = N // 60 // 60 % 24
minutes = N // 60 % 60

if minutes < 10:
    minutes = "0" + str(minutes)
seconds = N % 60
if seconds < 10:
    seconds = "0" + str(seconds)
print(hours, minutes, seconds, sep = ":")
