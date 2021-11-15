# Adaptive-Python
The course consists of few hundreds of programming assignments for Python, ranging from basics up to complex topics.

# 2.1 Squirrels and nuts
N squirrels found K nuts and decided to divide them equally. Determine how many nuts each squirrel will get.

<b>Input data format:</b>
There are two positive numbers N and K, each of them is not greater than 10000.

# 2.10 The sum of digits of a three-digit number
Given a three-digit integer (i.e. an integer from 100 to 999). Find the sum of its digits.

# 2.165 Repeated values
Write a program that takes a list of integers as input, and outputs the values that are repeated in it more than once.
You may need the list method sort to solve this problem.

<b>Input format:</b>
One line with integers, separated by a space.

<b>Output format:</b>
A line with integers, separated by a space. The numbers must not be repeated, the output order can be arbitrary.

# 2.18 Calculator
Write a simple calculator that reads the three input lines: the first number, the second number and the operation, after which it applies the operation to the entered numbers ("first number" "operation" "second number") and outputs the result to the screen. Note that the numbers can be real.

Supported operations: +, -, /, *, mod, pow, div; where
mod — taking the residue,
pow — exponentiation,
div — integer division.

If a user performs the division and the second number is 0, it is necessary to output the line "Division by 0!".

# 2.217 Power 3
Given a real positive number a and an integer number n.

Find a^n. You need to write the whole program with a recursive function power(a, n).

# 2.23 Floor-space of the room
Residents of the Malevia country often experiment with the plan of their rooms. Rooms can be triangular, rectangular and round. To quickly calculate the floorage it is required to write a program, which gets the type of the room shape and the relevant parameters as input - the program should output the area of the resulting room.
The value of 3.14 is used instead of the number π in Malevia.

<b>Input format used by the Malevians:</b>
- triangle
- a
- b
- c

where a, b and c — lengths of the triangle sides.

- rectangle
- a
- b

where a and b —lengths of the rectangle sides.

- circle
- r

where r — circle radius.

# 2.36 Distance
Write a program that inputs the distance between the two cities in miles and the travel time by bus in hours, and outputs the average speed of the bus.

# 2.4 MKAD
The length of the Moscow Ring Road (MKAD) is 109 kilometers. Biker Vasya starts from the zero kilometer of MKAD and drives with a speed of V kilometers per hour. On which mark will he stop after T hours?

<b>Input data format:</b>
The program gets integers V and T as input. If V > 0, then Vasya moves in a positive direction along MKAD, if the value of V < 0 – in the negative direction. 0 ≤ T ≤ 1000, -1000 ≤ V ≤ 1000.

<b>Output data format:</b>
The program should output an integer from 0 to 108 - the mark on which Vasya stops.

# 2.46 Fizz Buzz
Fizz Buzz is a classic programming problem. Here is its slightly modified version.

Write a program that takes the input of two integers: the beginning and the end of the interval (both numbers belong to the interval).

The program should output the numbers from this interval, but if the number is divisible by 3, you should output Fizz instead of it, if the number is divisible by 5 - output Buzz, and if it is divisible both by 3 and by 5 - output FizzBuzz.

Output each number or the word on a separate line.

# 2.5 Difference of times
Given the values of the two moments in time in the same day: hours, minutes and seconds for each of the time moments. It is known that the second moment in time happened not earlier than the first one. Find how many seconds passed between these two moments of time.

<b>Input data format:</b>
The program gets the input of the three integers: hours, minutes, seconds, defining the first moment of time and three integers that define the second moment time.

<b>Output data format:</b>
Output the number of seconds between these two moments of time.

# 2.6 Digital watches
Digital watches display time in the h:mm:ss format (from 0:00:00 to 23:59:59), i.e. first goes the number of hours, then goes the two-digit number of minutes, followed by the two-digit number of seconds. If necessary, number of minutes and seconds are filled by zeroes to a two-digit number.

N seconds passed from the beginning of the day. Output what the watches will display.

# 2.66 Palindrome
Given a string. Find whether it is a palindrome, i.e. it reads the same both left-to-right and right-to-left. Output “yes” if the string is a palindrome and “no” otherwise.

# 2.86 Containing the words
Input of the program is a line containing the words separated by a space. The program should output the information of lengths of words in the given line, from the shortest to the longest word (see the example).

A word is a sequence of arbitrary characters surrounded by spaces or line boundaries. Note that punctuation marks also belong to a word.

# 2.87 Login and password
You have login and password as integer numbers stored in the code as login and password variables. The user inputs two integers (the login and the password). If they match to one in the code - output "Login success", if the password doesn't match, but logins match, output "Wrong password", if login is wrong, output "No user with login XXXX found", where XXXX is the login, the user's just input.

<b>INPUT:</b>
Two integers, the first - login, the second - password.

<b>OUTPUT:</b>
"Login success" if both match, "Wrong password" if passwords do not match, but logins match and "No user with login XXXX found" if logins do not match (XXXX is the login, the user has input).

# 2.89 Uppercase
Input a single character and change its register. That is, if the lowercase letter has been entered – make it uppercase, and vice versa. Characters that are not Latin ones need to stay unchanged.

# 2.9 Next even number
Given a natural number N, not greater than 10000. Output the even number following this N.
