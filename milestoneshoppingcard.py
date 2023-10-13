print("Welcome to the Shopping Cart Program!") 



articles = []
def option1():
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of ''? "))
    article = {"item": item, "price": price}
    articles.append(article)
    print(f"{item} ${price} has been added to the cart.")

def option2():
    if not articles:
        print("The list is empty")
    else:
        print("The content of shopping cart are:")
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['item']} - ${article['price']}")

def option3():
    print("==================================")

    option2()
    if not articles:
        print("The are no items to delete")
        print("===================================")
        return
    try:
        index = int(input("Enter the number of the item you want to delete: ")) - 1
        if 0 <= index < len(articles):
            article_delete = articles.pop(index)
            print(f"{article_delete['item']} has been removed from the list of cart")
        else:
            print("Invalid item number")
    except ValueError:
        print("Please enter a valid number")
        print("===================================")

def option4():
    total = sum(article['price'] for article in articles)
    print(f"The total price of the items in the list is: ${total}")

def option5():
    print("Thank you, Goodbye")

while True:
    print("Please select one of the following: ")
    print("1.Add item \n2.View cart \n3.Remove item, \n4.Compute total, \n5.Quit")

    selection = input("Choose an option: ")
    if selection == "1":
        option1()
    elif selection == "2":
        option2()
    elif selection == "3":
        option3()
    elif selection == "4":
        option4()
    elif selection == "5":
        print("Thank you, Goodbye")
        break
    else:
        print("Option not valid. Please choose a valid option")