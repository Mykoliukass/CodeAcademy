# Create a program that allows user to Enter his/her name and Age
# Calculate the year in which user was born
# Print the answer to the Terminal

# from datetime import datetime 
# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# year = datetime.now().year
# print(year)
# print("Hello, ", name, "you're born in: ", (int(year)-age))

# Create a program that allows user to enter a full sentence
# print the sentence backwards
# print every second letter in the sentence
# sentence = input("Please input a sentence here: ")
# print(sentence[::-1])
# print(sentence[::2])

# Create a program that expects user to enter two numbers
# multiply those numbers and print the answer
# Create similar programs with other signs.

# a = float(input("Please provide a first number: "))
# b = float(input("Please provide a second number: "))
# print("Multiplication of these numbers is equal to: ", (a*b))
# print("Division of these numbers is equal to: ", (a/b))
# print("Division without a remainder of these numbers is equal to: ", (a//b))
# print("a into a power of b is equal to: ", (a**b))
# print("Remainder from the division of these numbers is equal to: ", (a%b))

# Create program that allows user to enter text
# Convert that text to Leet speak 1337
# print outcome

text = input("Please provide a text here: ")
text_1 = text.upper()
text_leet = text_1.replace('A', '4').replace('B', '8').replace('C', '<').replace('E', '3') \
    .replace('G', '6').replace('H', '#').replace('I', '1').replace('L', '|').replace('O', '0') \
    .replace('S', '$').replace('T', '7').replace('Z', '2')
print("Text changed into leet: ", text_leet)