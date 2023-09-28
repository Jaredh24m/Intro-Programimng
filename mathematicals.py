

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

# grade = int(input("What is your grade percent? "))

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# print(f"Your letter grade is: {letter}")

# if grade >=70:
#     print("Congratulations! You passed the class!")
# else:
#     print("Stay focused nd you'll get it next time!")

# grade = int(input("What is your grade percent? "))

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# #challenge 1
# sign = ""
# last_digit = grade % 10

# if last_digit >= 7:
#     sign = "+"
# elif last_digit < 3:
#     sign = "-"
# else:
#     sign = ""

# #challenge 2
# if grade >= 93:
#     sign = ""

# #challenge 3
# if letter =="F":
#     sign = ""

# print(f"Your letter grade is: {letter}")

# if grade >=70:
#     print("Congratulations! You passed the class!")
# else:
#     print("Stay focused nd you'll get it next time!")

type = input("You are walking through a dark forest and find two items: a 'MATCH' and a 'FLASHLIGHT'. Which one do you want to pick up? ")

if type.lower() == "match":
    print(f"In the middle of the roat halfway along the way a strong wind blew and it went out, you have to go back.")
elif type.lower() == "flashlight":
    print(f"You will continue walking through the dark forest")
else:
   print(f"You need to choose only a MATCH or FLASHLIGHT")

chose = input("You will continue walking and in the middle of the road you will find a cabin that you decide: 'FOLLOW THE PATH' OR 'ENTER THE CABIN'? ")

if chose.lower() == "follow the path":
    print(f"you will continue walking and you will find a cave")
    decision = input("It starts to rain, what do you choose: do you decide 'ENTER THE CAVE', 'WALK' through the dark forest in the rain or 'RETURN'? ")
    if decision.lower() == "enter the cave":
        print(f"They discover that it is very dark and you hear very loud breathing.")
    elif decision.lower() == "walk":
        print(f"The more you walk, the harder the rain starts and you can no longer see where to take shelter.")
    elif decision.lower() == "return":
        print(f"When you try to return you discover that you are lost and you don't know what to do.")
    else:
        print(f"At this point decisions are crucial")
elif chose.lower() == "enter the cabin":
    print(f"You enter the cabin and discover that there is light and the fireplace is lit.")
    decision_cabin = input("When you discover that there is light and the fireplace is on, what do you decide: 'LEAVE' immediately, 'INVESTIGATE' who lives in the cabin? ")
    if decision_cabin.lower() == "leave":
       print(f"When you leave the cabin you see a shadow coming towards you")
    elif decision_cabin.lower() == "investigate":
        print(f"When you enter the living room you hear someone coming down the stairs and your heart races.")
    else: 
        print(f"There is no turning back")
else:
    print(f"There is no way out only one decision")



# decision_cabin = input("When you discover that there is light and the fireplace is on, what do you decide: 'LEAVE' immediately, 'INVESTIGATE' who lives in the cabin? ")

# if decision_cabin.lower() == "leave":
#     print(f"When you leave the cabin you see a shadow coming towards you")
# elif decision_cabin.lower() == "investigate":
#     print(f"When you enter the living room you hear someone coming down the stairs and your heart races.")
# else: 
#     print(f"There is no turning back")