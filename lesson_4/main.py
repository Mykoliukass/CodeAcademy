# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = input("Please enter your name: ")
# surname = input("Please enter your surname: ")
# age = int(input("Plesase enter your age: "))
# if age >= 21:
#     print("You may enter our online casino.")
# else:
#     print("You are too young.")

# Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# privileged_users = ["Jonas","Petras","Kazys"]
# name = input("What is your name? ")
# if name in privileged_users:
#     print(f"Hello, Dear {name}, it is nice to have you here")
# else:
#     print("Welcome")

# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# first = float(input("Please enter your first number: "))
# second = float(input("Please enter your second number: "))
# if first == second:
#     print("They are equal")
# elif first > second:
#     print("First number is larger than the other.")
# else:
#     print("Second number is larger than the other.")

# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# x = float(input("Please enter your first number: "))
# y = float(input("Please enter your second number: "))
# sign = input("""Please enter a sign of the opperation you want to make between these two numbers. 
# Please note, that valid operations are: +, -, *, /, %, ^: """)
# result = 0
# if sign == "+":
#     result = x+y
# elif sign == "-":
#     result = x-y
# elif sign == "*":
#     result = x*y
# elif sign == "/":
#      if y !=0:
#         result = float(x/y)
#      else:
#         print("Cannot divide by zero")
#         exit()
# elif sign == "%":
#      if y !=0:
#         result = x%y
#      else:
#         print("Cannot divide by zero")
#         exit()
# elif sign == "^":
#     result = x**y
# else:
#     print(f"The operation you have provided cannot be done. We are not supporting the sign: {sign}")
#     exit()
# print("The answer of this calculation is: ", result)

# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
# import random
# random_number = random.randint(1,10)
# guess = False
# while guess == False:
#     guessed_number = input("Please try and guess the number I have in mind. It is between 1 and 10: ")
#     guessed_number = int(guessed_number)
#     if guessed_number == random_number:
#         guess = True
#         print(f"You guessed correctly! {guessed_number} indeed was my number!")
#     else: 
#         guess = False

import random as ran
random_number = ran.randint(1,10)
print("Please try and guess the number I have in mind. It is between 1 and 10. You have just one guess!")
guessed_number = int(input("What is your guess? "))
if guessed_number == random_number:
    print(f"You guessed correctly! {guessed_number} indeed was my number!")
else: 
    print(f"False, you lose. My number was {random_number}.")


# input_1 = input("First num: ")
# input_2 = input("Second num: ")
# input_3 = input("Third num: ")
# input_list = [input_1, input_2, input_3]
# print(input_list)
# input_into_a_touple = tuple(input_list)
# print(input_into_a_touple)


# Create a program, which takes 10 random numbers. The program should produce
# a list of non primary and tuple of primary numbers. After input is done, program should return the the mathematical
# differnce between the highest and lowest number from non primary numbers, and sum of primary numbers from tuple.

# input_by_user = input("""Please provide a list of 10 numbers, separate them with comma ",".
#  If you provide more than 10 numbers, I will pretend not to see them. """)
# input_into_a_list_str = input_by_user.split(",")
# input_into_a_list_ints = [int(item) for item in input_into_a_list_str]
# primary_list = []
# non_primary_list = []
# for num in input_into_a_list_ints:
#     if num <= 1:
#         print(f"Number {num} is neither a prime nor a regular number")
#     elif num == 2:
#         non_primary_list.append(num)
#     elif num % 2 == 0:
#         non_primary_list.append(num)
#     else:
#         is_prime = True
#         for a in range(3, int(num**0.5) + 1, 2):
#             if num % a == 0:
#                 non_primary_list.append(num)
#                 is_prime = False
#                 break
#         if is_prime:
#             primary_list.append(num)
# print("Prime: ", primary_list)
# print("difference of primes: ", max(primary_list) - min(primary_list))
# print("Non-Prime: ", primary_list)
# print("Non-Prime: ", sum(non_primary_list))

# from sympy import isprime
# input_into_a_list_ints = []
# for i in range(10):
#     number = int(input(f"Enter number {i+1}: "))
#     input_into_a_list_ints.append(number)
# primary_list = []
# non_primary_list = []
# for i in input_into_a_list_ints:
#     if isprime(i) == True:
#         primary_list.append(i)
#     else:
#         non_primary_list.append(i)
# print("Prime: ", primary_list)
# print("difference of primes: ", max(primary_list) - min(primary_list))
# print("Non-Prime: ", primary_list)
# print("Non-Prime: ", sum(non_primary_list))


# # Create a program, which takes 10 random numbers as user inputs.
# # The program should produce list of input values what are less than 50 and tuple of all other values.
# # After input is done, program should return the the mathematicaldiffernce between the highest and lowest number from list, and sum  from tuple.
# input_into_a_list_ints = []
# for i in range(10):
#     number = int(input(f"Enter number {i+1}: "))
#     input_into_a_list_ints.append(number)
# my_list = []
# my_tuple_will_be = []
# for i in input_into_a_list_ints:
#     if i <50:
#         my_list.append(i)
#     else:
#         my_tuple_will_be.append(i)
# my_tuple = tuple(my_tuple_will_be)
# print("List: ", my_list)
# print("difference of max and min in the list: ", max(my_list) - min(my_list))
# print("Tuple: ", my_tuple)
# print("Sum of the tuple: ", sum(my_tuple))

# a = 50
# b = int(input("Please provide a number: "))
# if b >= a:
#     print(b)
# else:
#     print(a)

# a = int(input("Please provide a first number (a): "))
# b = int(input("Please provide a second number (b): "))
# c = int(input("Please provide a third number (c): "))
# d = int(input("Please provide a fourth number (d): "))
# if a < b and b < c:
#     print(f"First condition met: {b}")
# elif a > c:
#     print(f"Second condition met: {a}")
# else:
#     print(f"Third condition met. First number: {a}. Second number: {b}. Third number: {c}. Fourth number: {d}")
