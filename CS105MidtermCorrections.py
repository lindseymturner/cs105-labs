# 1)
# for x in range(1,6):
#   print("This time through the loop, the value of x is " + str(x)
# X is an integer, but since we want to print a string, we have to convert x to a string.

# 2)
# Lists are helpful because they can have strings and integers together. They can also be edited at any time, allowing specific items to be changed, added, or removed.
# One disadvantage of lists is that they can take more time to run and take up more space.
# Dictionaries can store a pair of values, including a key (constant) and a value that corresponds to it. Dictionaries are helpful because the keys can be a string or an integer.
# The order of key value pairs doesn't matter. Dictionaries can be edited, i.e. the value corresponding to a key can be replaced.
# One disadvantage of dictionaries is that there can only be one value corresponding to each key.
# Dictionaries make it easy to look up elements, i.e. finding the value that corresponds to a specific key. Dictionaries take less time to run and take up less storage than lists.

# 3)
# The issue is that words containing "A" or "a" in them will be added to the Alist as well as the nonAlist because it is going through each letter of the name to determine if it is "A" or "a".
# For a name like "Alex", once it gets to the "l", it will put the name in the nonAlist.

# 4)
# First, we need to change the 2nd through 4th if statements to elif statements. We also need to add and second inequality to the elif statements to create a clear range for each letter grade.
#
# Rose_grade = 92
# if Rose_grade > 90:
#   print("Rose got an A")
# elif Rose_grade > 80 and Rose_grade <= 90:
#   print("Rose got a B")
# elif Rose_grade > 70  and Rose_grade <= 80:
#   print("Rose got an C")
# elif Rose_grade > 60 and Rose_grade <= 70:
#   print("Rose got a D")
# else:
#   print("Rose got a F")

# 5)
# def produce():
#   vegetables = {'eggplant': 5, 'squash': 7, 'arugula': 2}
#   while True:
#       choice = input("If you want to add produce, please type the vegetable, or STOP")
#       if choice == "STOP":
#           break
#
#       elif choice in vegetables:
#           vegetables[choice] += 1
#       else:
#           vegetables[choice] = 1
#   print(vegetables)
# produce()

# 6)
# def my_function(float_list):
#      sum_float = sum(float_list)
#      product_result = 1
#      for num in float_list:
#          product_result *= num
#      return sum_float, product_result
#
# float_list = [2.11, 6.7, 3.14, 84.175]
# sum_float, product_result = my_function(float_list)
# print("The sum of the floats is", sum_float)
# print("The product of the floats is", product_result)


# 7)
#
#
#
#
# def vacation(city):
#     city = input("Please enter a destination city")
#     if len(city) < 8:
#         return False
#     if "e" and "E" not in city:
#         return False
#     if city[3] == "i":
#         return False
#     if len(city) % 2 != 0:
#         return False
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in city:
#         if char in vowels:
#             count += 1
#     if count % 2 != 0:
#         return False
#     else:
#         return True
#
#
#     if vacation(city):
#         print("The Marsh Family will travel to", city)
#     else:
#         print("The Marsh Family will not travel to", city)
#
# 8)
#
# def my_function(n):
#     if n <= 0:
#         return []
#
#     my_list = []
#     for x in range(1, n + 1):
#         my_list.append(4 * x - 2)
#
#     print(my_list)
#     return my_list
#
#
# n = 13
# result = my_function(n)
#
# 9)
#
# def my_function():
#     bowling_scores = {}
#
#     while True:
#         user_input = input("Enter your name followed by a dash and then the best 3-digit bowling score you have ever played, when done type STOP")
#         if user_input == "STOP":
#             break
#
#         name, score = user_input.split("-")
#         score = int(score)
#         bowling_scores[name] = score
#
#     print(bowling_scores)
#
#
# my_function()
#
# 10)
#
# def harmonic_sum(n):
#     if n == 1:
#         return 1.0
#     else:
#         return 1.0 / n + harmonic_sum(n - 1)
#
#
# print(harmonic_sum(7))










