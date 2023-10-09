# Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)

# input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
# input_into_a_list = input_by_user.split(',')
# input_into_a_list_floats = [float(item) for item in input_into_a_list]
# sum_of_all_numbers = sum(input_into_a_list_floats)
# print("Sum of all the numbers that you have provided to me: ", sum_of_all_numbers)

# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

# input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
# input_into_a_list = input_by_user.split(',')
# input_into_a_list_floats = [float(item) for item in input_into_a_list]
# multiplication_of_all_numbers = 1.0
# for item in input_into_a_list_floats:
#     multiplication_of_all_numbers *= item
# print("Multiplication of all the numbers that you have provided to me: ", multiplication_of_all_numbers)

# Write a python program that gets maximum value from the list (all items are integers or floats in list, create a list yourself)

input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
input_into_a_list = input_by_user.split(',')
input_into_a_list_floats = [float(item) for item in input_into_a_list]
print("Sum of all the numbers that you have provided to me: ", max(input_into_a_list_floats))

# Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)

# input_by_user = input("Please provide a list of string, separate them with ',': ")
# input_into_a_list = input_by_user.split(',')
# concatenated_list = ""
# for a in input_into_a_list:
#     concatenated_list += f"{a} "
# print("Concatenation of all the strings that you have provided to me: ", concatenated_list)

# Create two lists and add them together, make sure it works the way you want it to.

# input_by_user = input("Please provide a list of string, integers or floats, separate them with ',': ")
# input_into_a_list = input_by_user.split(',')
# input_by_user_2 = input("Please provide another list of string, integers or floats, separate them with ',': ")
# input_into_a_list_2 = input_by_user_2.split(',')
# print("When you add these lists together you get this list: ", input_into_a_list + input_into_a_list_2)

# Write a python program that asks user to enter 3 integers and find the highest value entered.

# while True:
#     input_by_user = input("""Please provide a list of integers, separate them with ','. \n 
#     Please note, that if you will provide more than three digits, I will only check the first three.: """)
#     input_into_a_list = input_by_user.split(',')
#     if all(item.isdigit() for item in input_into_a_list[:3]):
#         input_into_a_list_integers = [int(item) for item in input_into_a_list[:3]]
#         print("highest integer you have provided was:", max(input_into_a_list_integers))
#         break
#     else:
#         print("You have entered something else, not three integers, please try again.")

# Try doing same exercises with tuples.

# Write a python program that sums up all items in the list (all items are integers or floats in list, create a list yourself)

# input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
# input_into_a_tuple = tuple(input_by_user.split(','))
# input_into_a_tuple_floats = [float(item) for item in input_into_a_tuple]
# sum_of_all_numbers = sum(input_into_a_tuple_floats)
# print("Sum of all the numbers that you have provided to me: ", sum_of_all_numbers)

# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

# input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
# input_into_a_tuple = tuple(input_by_user.split(','))
# input_into_a_tuple_floats = [float(item) for item in input_into_a_tuple]
# multiplication_of_all_numbers = 1.0
# for item in input_into_a_tuple_floats:
#     multiplication_of_all_numbers *= item
# print("Multiplication of all the numbers that you have provided to me: ", multiplication_of_all_numbers)

# Write a python program that gets maximum value from the list (all items are integers or floats in list, create a list yourself)

# input_by_user = input("Please provide a list of integers or floats, separate them with comma ',': ")
# input_into_a_tuple = tuple(input_by_user.split(','))
# input_into_a_tuple_floats = [float(item) for item in input_into_a_tuple]
# print("Sum of all the numbers that you have provided to me: ", max(input_into_a_tuple_floats))

# Write a python program that concatenates all strings in the list (all items are strings, create a list yourself)

# input_by_user = input("Please provide a list of string, separate them with ',': ")
# input_into_a_tuple = tuple(input_by_user.split(','))
# concatenated_tuple = ""
# for a in input_into_a_tuple:
#     concatenated_tuple += f"{a} "
# print("Concatenation of all the strings that you have provided to me: ", concatenated_tuple)

# Create two lists and add them together, make sure it works the way you want it to.

# input_by_user = input("Please provide a list of string, integers or floats, separate them with ',': ")
# input_into_a_tuple = tuple(input_by_user.split(','))
# input_by_user_2 = input("Please provide another list of string, integers or floats, separate them with ',': ")
# input_into_a_tuple_2 = tuple(input_by_user_2.split(','))
# joined_tuple = input_into_a_tuple + input_into_a_tuple_2
# print("When you add these lists together you get this list: ", joined_tuple)

# Write a python program that asks user to enter 3 integers and find the highest value entered.

# while True:
#     input_by_user = input("""Please provide a list of integers, separate them with ','. \n 
#     Please note, that if you will provide more than three digits, I will only check the first three.: """)
#     input_into_a_tuple = tuple(input_by_user.split(','))
#     if all(item.isdigit() for item in input_into_a_tuple[:3]):
#         input_into_a_tuple_integers = [int(item) for item in input_into_a_tuple[:3]]
#         print("highest integer you have provided was:", max(input_into_a_tuple_integers))
#         break
#     else:
#         print("You have entered something else, not three integers, please try again.")

# Useris 4 kartus turi ivest skaiciu, juos sudet i lista ir isprintinti listo max, 