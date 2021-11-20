# Adaptive-Python
The course consists of few hundreds of programming assignments for Python, ranging from basics up to complex topics.

## 1 Squirrels and nuts
N squirrels found K nuts and decided to divide them equally. Determine how many nuts each squirrel will get.

## 4 MKAD
The length of the Moscow Ring Road (MKAD) is 109 kilometers. Biker Vasya starts from the zero kilometer of MKAD and drives with a speed of V kilometers per hour. On which mark will he stop after T hours?

## 5 Difference of times
Given the values of the two moments in time in the same day: hours, minutes and seconds for each of the time moments. It is known that the second moment in time happened not earlier than the first one. Find how many seconds passed between these two moments of time.

## 6 Digital watches
Digital watches display time in the h:mm:ss format (from 0:00:00 to 23:59:59), i.e. first goes the number of hours, then goes the two-digit number of minutes, followed by the two-digit number of seconds. If necessary, number of minutes and seconds are filled by zeroes to a two-digit number.

N seconds passed from the beginning of the day. Output what the watches will display.

## 9 Next even number
Given a natural number N, not greater than 10000. Output the even number following this N.

## 10 The sum of digits of a three-digit number
Given a three-digit integer (i.e. an integer from 100 to 999). Find the sum of its digits.

## 11 The number of tens
Given a non-negative integer N (0 ≤ N ≤ 1000000), find the number of tens in it (i.e. next to last digit of the number). If there is no next to last digit, you can consider that the number of tens equals to zero.

## 18 Calculator
Write a simple calculator that reads the three input lines: the first number, the second number and the operation, after which it applies the operation to the entered numbers ("first number" "operation" "second number") and outputs the result to the screen. Note that the numbers can be real.

Supported operations: +, -, /, *, mod, pow, div; where
mod — taking the residue,
pow — exponentiation,
div — integer division.

If a user performs the division and the second number is 0, it is necessary to output the line "Division by 0!".

## 23 Floor-space of the room
Residents of the Malevia country often experiment with the plan of their rooms. Rooms can be triangular, rectangular and round. To quickly calculate the floorage it is required to write a program, which gets the type of the room shape and the relevant parameters as input - the program should output the area of the resulting room.
The value of 3.14 is used instead of the number π in Malevia.

## 24 Robot
The robot moves down the office in the Bioinformatics Institute. Recently, students from the programmers group wrote a program for this robot, according to which when robot enters the room, he counts the number of programmers present in this room and says it aloud: "n programmers".

In order for it to sound correctly, for each nn you need to use the correct word ending.

Write a program, reading an integer nn (non-negative one) from the user input, outputting this number together with the correctly changed word "programmer", so that the robot could correctly communicate with people, for example: 1 programmer, 2 programmers, 5 programmers.

There can be many programmers in one room. Make sure that your program works correctly for all the cases until 1000 persons

## 26 Direction
Write a program, which reads the number of direction (1 – up, 2 – down, 3 – left, 4 – right, 0 – stay) and outputs the text «move up» (or «move down», or «move left», or «move right», or «do not move» depending on the entered number). If it is a number that does not belong to any of the listed directions, the program should output: «error!»

## 30 Chess board
You are given coordinates of two queens on a chess board. Find out, whether they hit each other or not.

## 31 Heron's formula
Many years ago when Paul went to school, he did not like the Heron's formula to calculate the area of a triangle, because he considered it very complex. Once he decided to help all school students: to write and distribute the program, calculating the area of a triangle by its three sides.

However, there was a problem: as Paul did not like the formula, he did not memorize it. Help him finish this act of kindness and write the program, calculating the area of a triangle by the transferred length of its sides, in accordance with the Heron's formula:

S = sqrt(p(p − a)(p − b)(p − c))

where p = (a + b + c) / 2 – half-perimeter of the triangle. On the input, the program has integers, and the output should be a real number corresponding to the area of the triangle.

## 35 Quadratic equation
Given real numbers a, b, c, where a ≠ 0.

Solve the quadratic equation ax^2 + bx + c = 0 and output all of its roots.

If the equation has two roots, output these two roots in ascending order; if one root - output a single number; if no roots – do not output anything.

## 36 Distance
Write a program that inputs the distance between the two cities in miles and the travel time by bus in hours, and outputs the average speed of the bus.

## 46 Fizz Buzz
Fizz Buzz is a classic programming problem. Here is its slightly modified version.

Write a program that takes the input of two integers: the beginning and the end of the interval (both numbers belong to the interval).

The program should output the numbers from this interval, but if the number is divisible by 3, you should output Fizz instead of it, if the number is divisible by 5 - output Buzz, and if it is divisible both by 3 and by 5 - output FizzBuzz.

Output each number or the word on a separate line.

## 49 Sum of all elements
Find the sum of all elements of the sequence, ending with the number 0.

The number 0 itself is not included into the sequence and serves as a sign of cessation.

## 66 Palindrome
Given a string. Find whether it is a palindrome, i.e. it reads the same both left-to-right and right-to-left. Output “yes” if the string is a palindrome and “no” otherwise.

## 86 Containing the words
Input of the program is a line containing the words separated by a space. The program should output the information of lengths of words in the given line, from the shortest to the longest word (see the example).

A word is a sequence of arbitrary characters surrounded by spaces or line boundaries. Note that punctuation marks also belong to a word.

## 87 Login and password
You have login and password as integer numbers stored in the code as login and password variables. The user inputs two integers (the login and the password). If they match to one in the code - output "Login success", if the password doesn't match, but logins match, output "Wrong password", if login is wrong, output "No user with login XXXX found", where XXXX is the login, the user's just input.

## 89 Uppercase
Input a single character and change its register. That is, if the lowercase letter has been entered – make it uppercase, and vice versa. Characters that are not Latin ones need to stay unchanged.

## 154 An algorithm to decode strings
Run-length encoding is the basic algorithm of data compression.

In this problem, we will implement an algorithm to decode strings, encoded with one of its simplest versions.

On the input, the algorithm has a string containing the characters of the Latin alphabet. This string is split into the so-called "series", which are encoded by a number-symbol pair or just a symbol (in this case, the number is considered equal to one). The result must contain the series in the same order, in which they occur in the original string, and each series is disclosed into the sequence of characters of a corresponding length.

For example, let’s take the string

## 160 Position in list
Write a program, which reads the list of numbers lstlst from the first line and the number xx from the second line of the input; and outputs all positions, on which the number xx can be found in the given list lstlst.

The positions are numbered from zero; if the number xx is not present in the list - output "Missing" (without quotation marks, starting from the capital letter).

Output the positions in a single line, by the ascending absolute values.
```
3ab4c2CaB
```
Split it down into series
```
3a b 4c 2C a B
```
Then transform the series and obtain the original encoded string:
```
aaabccccCCaB
```

## 165 Repeated values
Write a program that takes a list of integers as input, and outputs the values that are repeated in it more than once.
You may need the list method sort to solve this problem.

## 204 Distance
Given the four real numbers: x1, y1, x2, y2. Write the function distance(x1, y1, x2, y2), calculating the distance between the point (x1. y1) and point (x2, y2).

Read the four real numbers and output the result of this function's call.

## 217 Power 3
Given a real positive number a and an integer number n.

Find a^n. You need to write the whole program with a recursive function power(a, n).

## 296 Chess board
You are given two coordinates on a chess board of the first queen and two of the second. Find out, whether two queens hit each other or not.

## 323 HTML-pages
There are two HTML-pages – A and B.
From A we can go to B in one step, if inside A there is a link to B, i.e. inside A there is a tag \<a href="B">, possibly with additional parameters inside the tag.

From A we can go to B in two steps, if there is such document C, that from A to C we can go in one step, and from C to B we can go in one step.

On input your program gets two lines, containing the URLs to the two documents A and B.
Output Yes, if you can go from A to B for two steps, otherwise output No.
  
Please note that not all links inside the HTML pages can lead to an existing HTML pages.
