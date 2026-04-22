print("select your ride: ")
print("1. bike")
print("2. car")                      

choice = int(input("enter your choice: "))
if choice == 1:
    print("what type of bike do you want to choose? ")
    print("1. sports bike")
    print("2. cruiser bike")

    choice2 =int(input("enter your choice: "))
    if choice2 == 1:
        print("you have selected sports bike")
    elif choice2 == 2:
        print("you have selected cruiser bike")
    else:
        print("invalid choice")
elif choice == 2:
    print("what type of car do you want to choose? ")
    print("1. lamborghini")
    print("2. suv")

    choice3 = int(input("enter your choice: "))
    if choice3 == 1:
        print("you have selected lamborghini")
    elif choice3 == 2:
        print("you have selected suv")
    else:
        print("invalid choice")

else:
    print("invalid choice")
