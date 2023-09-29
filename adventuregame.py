#1 scenery
type = input("You are walking through a dark forest and find two items: a 'MATCH' and a 'FLASHLIGHT'. Which one do you want to pick up? ")

if type.lower() == "match":
    print(f"In the middle of the roat halfway along the way a strong wind blew and it went out, you have to go back.")
    #5 scenery
    idea = input("When you return you find another match that you decide to make: LIGHT IT and follow the path or MAKE A FIRE to spend the night?")
    if idea.lower() == "light it":
        print(f"Bad idea with the wind that makes it would turn it off again and you would be left in the dark")
    elif idea.lower() == "make a fire":
        print(f"You would be safe at night because animals don't like fire.")
elif type.lower() == "flashlight":
    print(f"You will continue walking through the dark forest")
    #2 scenery
    chose = input("You will continue walking and in the middle of the road you will find a cabin that you decide: 'FOLLOW THE PATH' OR 'ENTER THE CABIN'? ")

    if chose.lower() == "follow the path":
        print(f"you will continue walking and you will find a cave")
    #3 scenery
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
        #4 scenery
        decision_cabin = input("When you discover that there is light and the fireplace is on, what do you decide: 'LEAVE' immediately, 'INVESTIGATE' who lives in the cabin? ")
        if decision_cabin.lower() == "leave":
            print(f"When you leave the cabin you see a shadow coming towards you")
        elif decision_cabin.lower() == "investigate":
            print(f"When you enter the living room you hear someone coming down the stairs and your heart races.")
        else: 
            print(f"There is no turning back")
    else:
        print(f"You need to choose only a MATCH or FLASHLIGHT")

else:
    print(f"There is no way out only one decision")