import random #importing module
playing = True #variable to check if the player wants to play again
number = str(random.randint(0, 9)) #generating a random number between 1 and 100

print("i will generate a random number between 0 to 9, you have to guess it")
print("the game ends when you get 1 hero")

while playing:
    guess = input("GIVE ME YOUR BEST GUESS!!\n")
    if number == guess:
        print("YOU ARE A HERO!!")
        print("the number was " + number)
        break

    else:
        print("YOUR GUESS IS NOT RIGHT, TRY AGAIN!!\n")
        