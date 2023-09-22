child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? ")) 
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? ")) 
subtotal = (child_meal * children) + (adult_meal * adults) 
print(f"\nSubtotal: ${subtotal:.2f}\n ")

percentage = float(input("What is the sales tax rate? "))
sales_tax = percentage * subtotal / 100
total = subtotal + sales_tax
print(f"Sales tax: ${sales_tax:.2f} ")
print(f"Total: {total:.2f}\n ")

payment = int(input("What is the payment amount? "))
change = payment - total
print(f"Change: ${change:.2f}")