first = input("First Name: ")
last = input("Last Name: ")
email = input("Email Adres: ")
phone = input("Phone number: ")
job_title = input ("Job Title: ")
id = input("Id Number: ")
hair_color = input("Hair Color: ")
eye_color = input("Eye color: ")
month = input("starting Month: ")
training = input("Complete aditional trainin?")

print("\n The Id Card is: ")
print("-----------------------------------")
print(f"{last.upper()} {first.capitalize()}")
print(job_title.capitalize())
print(f"ID: {id}")
print()
print(email.lower())
print(phone)
print()
print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
print("-----------------------------------")