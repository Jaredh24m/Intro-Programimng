

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

# type = input("You are walking through a dark forest and find two items: a 'MATCH' and a 'FLASHLIGHT'. Which one do you want to pick up? ")

# if type.lower() == "match":
#     print(f"In the middle of the roat halfway along the way a strong wind blew and it went out, you have to go back.")
# elif type.lower() == "flashlight":
#     print(f"You will continue walking through the dark forest")
# else:
#    print(f"You need to choose only a MATCH or FLASHLIGHT")

# chose = input("You will continue walking and in the middle of the road you will find a cabin that you decide: 'FOLLOW THE PATH' OR 'ENTER THE CABIN'? ")

# if chose.lower() == "follow the path":
#     print(f"you will continue walking and you will find a cave")
#     decision = input("It starts to rain, what do you choose: do you decide 'ENTER THE CAVE', 'WALK' through the dark forest in the rain or 'RETURN'? ")
#     if decision.lower() == "enter the cave":
#         print(f"They discover that it is very dark and you hear very loud breathing.")
#     elif decision.lower() == "walk":
#         print(f"The more you walk, the harder the rain starts and you can no longer see where to take shelter.")
#     elif decision.lower() == "return":
#         print(f"When you try to return you discover that you are lost and you don't know what to do.")
#     else:
#         print(f"At this point decisions are crucial")
# elif chose.lower() == "enter the cabin":
#     print(f"You enter the cabin and discover that there is light and the fireplace is lit.")
#     decision_cabin = input("When you discover that there is light and the fireplace is on, what do you decide: 'LEAVE' immediately, 'INVESTIGATE' who lives in the cabin? ")
#     if decision_cabin.lower() == "leave":
#        print(f"When you leave the cabin you see a shadow coming towards you")
#     elif decision_cabin.lower() == "investigate":
#         print(f"When you enter the living room you hear someone coming down the stairs and your heart races.")
#     else: 
#         print(f"There is no turning back")
# else:
#     print(f"There is no way out only one decision")



# decision_cabin = input("When you discover that there is light and the fireplace is on, what do you decide: 'LEAVE' immediately, 'INVESTIGATE' who lives in the cabin? ")

# if decision_cabin.lower() == "leave":
#     print(f"When you leave the cabin you see a shadow coming towards you")
# elif decision_cabin.lower() == "investigate":
#     print(f"When you enter the living room you hear someone coming down the stairs and your heart races.")
# else: 
#     print(f"There is no turning back")

# number = int(input("Please type a positive number: "))

# while number <0:
#     print(f"Sorry,this is a negative number. Please try again")
#     number = int(input("Please type a positive number: "))

# print(f"The number is: {number} ")

# answer = ""

# while answer != "yes":
#     answer = input("May I have a piece of candy? ")

# print("Thank you")

# items = ["crayon", "scissors", "paper", "glotter glue", "markers", "pens"]
# for item in items:
#     print(f"The item is: {item}")

# colors = ["red", "blue", "green", "yellow"]
# for color in colors:
#     print(color)
    
# for i in range (1,9):
#     print(i)

# for i in range (2, 21, 2):
#     print(i)

# first_name = "Brigham"
# for letter in first_name:
#     print(f"The letter is: {letter}")

# word = "Commitment"
# favorite_letter = input("What is your favorite letter? ")
# for letter in word:
#     if letter.lower() == favorite_letter.lower():
#         print(letter.upper(), end="")
#     else:
#         print(letter.lower(), end="")
# print()

# for letter in word:
#     if letter.lower() == favorite_letter.lower():
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")
# print()


import random

# magic_number = random.randint(1,100)
# guess = 2
# while guess != magic_number:
#     guess = int(input("What is your guess? "))

#     if guess < magic_number:
#         print("Higher")
#     elif guess > magic_number:
#         print("Lower")
#     else:
#         print("You guessed it!")

# keep_playing = "yes"

# while keep_playing == "yes":
#     magic_number = random.randint(1,100)
#     guess_count = 0
#     guess = -1
#     while guess != magic_number:
#         guess = int(input("What is your guess? "))
#         guess_count = guess_count + 1
#         if guess < magic_number:
#             print("Higher")
#         elif guess > magic_number:
#             print("Lower")
#         else:
#             print("You guessed it!")
#     print(f"It took you {guess_count} guesses")
#     keep_playing = input("Would you like to play again (yes/no)? ")
# print("Thank you for playing. Goodbye.")

# hint = ['_', '_', '_', '_', '_', '_']
# hint_result = ' '.join(hint) 

# secret = "mosiah"
# guess_count = 0

# print("Welcome to the word guessing game!")

# print(f"Your hint is:{hint_result}")
# guess_word = input("What is your guess? ")

# while (secret != guess_word):
#    if (len(secret) != len(guess_word)):
#       print()
#       print("Sorry, the guess must have the same number of letters as the secret word.")
#       guess_word = input("What is your guess? ")
#    else: 
#       for i in range(len(secret)):
#          for j in range(len(guess_word)):
#             # print(f"{i} - {j}"")
#             # print(f"{guess_word[i]} - {secret_word[j]})
#             if (list(guess_word)[i] == list(secret)[j]):
#                hint[i] = guess_word[i]
#                hint_result = " ".join(hint)
#       guess_count = guess_count + 1
#       print(f"Your hint is: {hint_result}")
#       guess_word = input("What is your guess? ")
# print(f"It took you {guess_count} guesses")
# print("Thank you for playing. Goodbye.")

# friends = []


# new_friend = ""
# while new_friend != "end":
#     new_friend = input("Type the name of a friend: ")
#     friends.append(new_friend)

# # friends.append("Mathew")
# # friends.append("Mark")
# # friends.append("Luke")
# # friends.append("John")
# # friends.append("Mathew")
# print()
# print("Your friends are: ")

# for friend in friends:
#     print(friend)

# friends = []
# name = None
# while name != "end":
#     name = input("Type the name of a friend: ")
#     if name != "end":
#         friends.append(name)
# print()
# print("Your friends are:")
# for friend in friends:
#     print(friend)

# print("Please enter the items of the shoping list (type: quit to finish):")

# shopping_list = []
# item = None
# while item != "quit":
#     item = input("Item: ")
#     if item != "quit":
#         shopping_list.append(item)
# print("\nThe shopping list is:")
# for item in shopping_list:
#     print(item)
# print("\nThe shopping list with indexes is:")
# for i in range(len(shopping_list)):
#     item = shopping_list[i]
#     print(f"{i}. {item}")
# print()
# index = int(input("Which item would you like to change? "))
# new_item = input("What is the new item? ")

# shopping_list[index] = new_item

# print("\nThe shopping list with indexes is:")
# for i in range(len(shopping_list)):
#     item = shopping_list[i]
#     print(f"{i}. {item}")



# print("Enter a list of numbers, type 0 when you finished.")
# numbers = []
# number = -1
# while number != 0:
#     number = int(input("Enter number: "))
#     if number != 0:
#         numbers.append(number)

# sum = 0
# for number in numbers:
#     sum += number

# print(f"The sum is: {sum}")

# count = len(numbers)
# average = sum / count

# print (f"The average is: {average}")

# best_so_far = -1
# for number in numbers:
#     if number > best_so_far:
#         best_so_far = number

# print(f"The largest number is: {best_so_far}")

# smallest_so_far = 99999999999
# for number in numbers:
#     if number > 0 and number < smallest_so_far:
#         smallest_so_far = number

# print(f"The smallest positive number is: {smallest_so_far}")
# sorted_list = sorted(numbers)

# print("The stored list is:")
# for number in sorted_list:
#     print(number)


# print("Welcome to the Shopping Cart Program!") 

# print("1.Add item \n2.View cart \n3.Remove item, \n4.Compute total, \n5.Quit")
# action = None
# print("Please select one of the following: ")
# for i in range(len(action_list)):
#     action = action_list[i]
#     print(f"{i}. {action}")
# while action != "quit":
#     action = input("Please enter an action: ")
#     if action != "quit":
#         action_list.append(action)
# while action != "Add item":
#     index = input("Which item would you like to add? ")
#     index = int(input("Which item would you like to add? "))

# def display_regular(message):
#     print(message)
# def display_uppercase(message):
#     new_message = message.upper()
#     print(new_message)
# def display_lowercase (massage):
#     new_message = massage.lower()
#     print(new_message)

# user_message = input("Whats is your message? ")

# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)

# def celsius_to_fahrenheit(celsius):
#     """Convert Celsius temperature to Fahrenheit."""
#     return (celsius * 9/5) + 32

# def calculate_wind_chill(temperature, wind_speed):
#     """Calculate wind chill based on temperature (in Fahrenheit) and wind speed (in mph)."""
#     wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
#     return wind_chill

# # Input temperature from the user
# temp_input = input("Enter temperature (e.g., 25C or 77F): ")

# if temp_input[-1] == 'C':
#     celsius_temperature = float(temp_input[:-1])
#     fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
# else:
#     fahrenheit_temperature = float(temp_input[:-1])

# # Display wind chill for wind speeds from 5 to 60 mph, in 5 mph increments
# print("\nWind Chill for Various Wind Speeds:")
# print(f"Temperature: {fahrenheit_temperature:.2f} °F")
# print("\nWind Speed (mph)\tWind Chill (°F)")
# print("-" * 35)

# for wind_speed in range(5, 61, 5):
#     wind_chill = calculate_wind_chill(fahrenheit_temperature, wind_speed)
#     print(f"{wind_speed}\t\t\t{wind_chill:.2f}")

# def celsius_to_fahrenheit(celsius):
#     """Convert Celsius temperature to Fahrenheit."""
#     return (celsius * 9/5) + 32

# def calculate_wind_chill(temperature, wind_speed):
#     """Calculate wind chill based on temperature (in Fahrenheit) and wind speed (in mph)."""
#     wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
#     return wind_chill

# # Input temperature from the user
# temp_input = input("Enter temperature (e.g., 25C or 77F): ")

# if temp_input[-1] == 'C':
#     celsius_temperature = float(temp_input[:-1])
#     fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
# else:
#     fahrenheit_temperature = float(temp_input[:-1])

# # Display wind chill for wind speeds from 5 to 60 mph, in 5 mph increments
# print("\nWind Chill for Various Wind Speeds:")
# print(f"Temperature: {fahrenheit_temperature:.2f} °F")
# print("\nWind Speed (mph)\tWind Chill (°F)")
# print("-" * 35)

# for wind_speed in range(5, 61, 5):
#     wind_chill = calculate_wind_chill(fahrenheit_temperature, wind_speed)
#     print(f"{wind_speed}\t\t\t{wind_chill:.2f}")

# def calculate_wind_chill(temperature, wind_speed):
#     wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
#     return wind_chill

# # Input temperature and unit from the user
# temperature = float(input("What is the temperature? "))
# unit = input("Fahrenheit or Celsius (F/C)? ")

# if unit.lower() == 'c':
#     temperature = (temperature * 9/5) + 32

# print(f"At temperature {temperature:.1f}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature, 5):.2f}F")
# for wind_speed in range(10, 61, 5):
#     print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {calculate_wind_chill(temperature, wind_speed):.2f}F")

# def calculate_wind_chill(temperature, wind_speed):
#     wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
#     return wind_chill

# # Input temperature and unit from the user
# temperature = float(input("What is the temperature? "))
# unit = input("Fahrenheit or Celsius (F/C)? ")

# if unit.lower() == 'c':
#     temperature_fahrenheit = (temperature * 9/5) + 32
#     print(f"At temperature {temperature:.1f}C, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature_fahrenheit, 5):.2f}F")
#     for wind_speed in range(10, 61, 5):
#         print(f"At temperature {temperature:.1f}C, and wind speed {wind_speed} mph, the windchill is: {calculate_wind_chill(temperature_fahrenheit, wind_speed):.2f}F")
# else:
#     print(f"At temperature {temperature:.1f}F, and wind speed 5 mph, the windchill is: {calculate_wind_chill(temperature, 5):.2f}F")
#     for wind_speed in range(10, 61, 5):
#         print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {calculate_wind_chill(temperature, wind_speed):.2f}F")

def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9/5) + 32

def calculate_wind_chill(temperature, wind_speed):
    """Calculate wind chill based on temperature (in Fahrenheit) and wind speed (in mph)."""
    wind_chill = 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

def main():
    # Input temperature and unit from the user
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or Celsius (F/C)? ").lower()

    if unit == 'c':
        temperature = celsius_to_fahrenheit(temperature)

    # Display wind chill for wind speeds from 5 to 60 mph, in 5 mph increments
    print("\nWind Chill for Various Wind Speeds:")
    print(f"Temperature: {temperature:.1f}F")
    print("\nWind Speed (mph)\tWind Chill (°F)")
    print("-" * 35)

    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"{wind_speed}\t\t\t{wind_chill:.2f}F")

if __name__ == "__main__":
    main()