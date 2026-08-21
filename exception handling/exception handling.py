#using a try and except
try:
    number = int(input("Please enter a number: "))
    print("the number you entered is:", number)
#using value error
except ValueError as ex:
    print("exception:", ex)


    