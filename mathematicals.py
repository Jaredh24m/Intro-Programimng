

# cars = 3
# people = 8
# people_per_car = people / cars
# print(f"There are {people_per_car:.1f} people in each car. ")
# print(f"There are {people_per_car:.2f} people in each car. ")
# print(f"There are {people_per_car:.3f} people in each car.\n ")

# distance =  9 * 1205 * 18
# print(f"The distance is: {distance:.3e} meters. ")
# print(f"The distance is: {distance:.6e} meters.\n ")

# big_number = 123456789
# print(f"The number is: {big_number}")
# print(f"The number is: {big_number:,}")
# print(f"The number is: {big_number:_}\n")

# radius = 5
# area = math. pi * (radius ** 2)
# print(f"The are is: {area}\n")

# weight = 1.65
# lower = math.floor (weight)
# print(lower)
# higher = math.ceil (weight)
# print(higher)

# degrees_f = float(input("What is the temperature in Fahrenheit? "))
# degrees_c = (degrees_f - 32) * 5/9
# print(f"The temperature un Celsius is {degrees_c} degrees.\n ")

# x = 2
# y = 3
# z = 4
# w = x + y * z
# print(w)

# x = input("First: ")
# y = input("Second: ")

# z = x + y

# print(z)

# dolls = 5

# print("There are " + dolls + " dolls")

# side = float(input("What is the lenght of a side of the square? "))
# area = side ** 2
# print(f"The area of the square is: {area} ")

# lenght = float(input("What is the Lenght of the rectangule? "))
# width = float(input("What is the width of the rectangule? "))
# area = lenght * width
# print(f"The area of th rectangule is: {area} ")

# radius = float(input("What is the radio of the circle? "))
# area = math. pi * (radius ** 2)
# print(f"The area of the circle is: {area}")

# radius = float(input("What is the radio of the circle? "))
# area = 3.14 * (radius ** 2)
# print(f"The area of the circle is: {area}")

# value = float(input("What is the value to be used? "))
# area_square = value ** 2
# area_circle = math. pi *(value * 2)
# volume_cube = value ** 3
# volume_sphere = (4 / 3) * math. pi * (value ** 3)
# print(f"Area of square is: {area_square} ")
# print(f"Area of a circle is: {area_circle} ")
# print(f"Area of the cube is: {volume_cube} ")
# print(f"area of the sphere is: {volume_sphere}")

# Area of the Square
# side = float(input("What is the length of a side of the square (in cm)? "))
# area = side ** 2
# print(f"The area of the square is: {area} cm^2")
# print(f"the area of the square is: {area / 10000} m^2")

# Area of the rectangule
# lenght = float(input("What is the Lenght of the rectangule? "))
# width = float(input("What is the width of the rectangule? "))
# area = lenght * width
# print(f"The area of th rectangule is: {area} cm^2")
# print(f"The area of th rectangule is: {area / 10000} m^2")

# # Area of the circle
# radius = float(input("What is the radio of the circle? "))
# area = 3.14 * (radius ** 2)
# print(f"The area of the circle is: {area} cm^2")
# print(f"The area of the circle is: {area / 10000} m^2")

# child_meal = float(input("What is the price of a child's meal? "))
# adult_meal = float(input("What is the price of an adult's meal? "))
# drinks_price = float(input("What is the price of the drinks? ")) 
# desserts_price = float(input("Whats is the price of the desserts"))
# children = int(input("How many children are there? "))
# adults = int(input("How many adults are there? "))
# drinks = int(input("How many drinks are there? ")) 
# desserts = int(input("how many desseerts are there? "))
# subtotal = (child_meal * children) + (adult_meal * adults) + (drinks_price * drinks) + (desserts_price * desserts)
# print(f"\nSubtotal: ${subtotal:.2f}\n ")

# percentage = float(input("What is the sales tax rate? "))
# sales_tax = percentage * subtotal / 100
# total = subtotal + sales_tax
# print(f"Sales tax: ${sales_tax:.2f} ")
# print(f"Total: {total:.2f}\n ")

# payment = int(input("What is the payment amount? "))
# change = payment - total
# print(f"Change: ${change:.2f}")

# price = input("How much did you pay? ")
# price = float(price)

# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0    
# print("Tax rate is: " + str(tax))

# country = input("Enter de name of your country: ")
# if country.lower == "canada":
#     print("So you must like hockey!")
# else:
#     print("You are not from Canada")

# province = input("What province do you live in? ")
# tax = 0 

# if province == "Alberta":
#     tax = 0.05
# elif province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

# province = input("What province do you live in? ")
# tax = 0 

# if province == "Alberta" or province == "Nunavut":
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

# province = input("What province do you live in? ")
# tax = 0 

# if province in ("Alberta", "Nunavut", "Yukon"):
#     tax = 0.05
# elif province == "Ontario":
#     tax = 0.13
# else:
#     tax = 0.15
# print(tax)

# first = int(input("Whats is the first number? "))
# second = int(input("What is the secind number? "))
# if first > second:
#     print("The first number is greater")
# else:
#     print("The first number is not greater")
# if first == second:
#     print("The numbers are equal")
# else:
#     print("The numbers are not equal") 
# if second > first:
#     print("The second number is greater")
# else:
#     print("The second number is not greater")

# print()

# user_animal = input("What is your favorite animal? ")
# if user_animal.lower() == "eagle":
#     print("That's my favorite animal too!")
# else:
#     print("That one is not my favorite")

# A student makes honour roll if their average is >=85
# and their lowest grade is not below 75
# gpa = float(input("What was your Grade Point Avarege? "))
# lowest_grade = input("What was your lowest grade? ")
# lowest_grade = float(lowest_grade)

# if gpa >= .85:
#     if lowest_grade >= .70:
#         print("You made the honour roll")

# print("For each these questions, please provide a 1-10 rating: ")

# loan_size = int(input("How large is the loan? "))
# credit = int(input("How good is your history? "))
# income = int(input("How high is your income? "))
# down_payment = int(input("How large is your down payment? "))

# should_loan = False

# if loan_size >= 5:
#     if credit >= 7 and income >= 7:
#         should_loan = True
#     elif credit >= 7 or income >= 7:
#         if down_payment >= 5:
#             should_loan = True
#         else:
#             should_loan = False
#     else :
#         should_loan = False
# else:
#     if credit < 4:
#         should_loan = False
#     else:
#         if income >= 7 or down_payment >= 7:
#             should_loan = True
#         elif income >= 4 and down_payment >= 4:
#             should_loan = True
#         else:
#             should_loan = False
# if should_loan:
#     print("The decision is yes. This is a good loan. ")
# else:
#     print("The decision is no. You should not loan this money. ")