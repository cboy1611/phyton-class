import random

secret = random.randint(1, 50)
attempts = 5

print("Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 50.")
print(f"You have {attempts} attempts to guess it.")

while attempts > 0:
    guess_input = input("Enter your guess: ")

    if not guess_input.isdigit():
        print("Please enter a valid whole number between 1 and 50.")
        continue

    guess = int(guess_input)
    if guess < 1 or guess > 50:
        print("Your guess must be between 1 and 50.")
        continue

    if guess == secret:
        print("🎉 Correct! You guessed the secret number!")
        break

    attempts -= 1
    hearts = "❤️" * attempts if attempts > 0 else ""
    distance = abs(secret - guess)

    if distance <= 2:
        hint = "Very close!"
    elif distance <= 5:
        hint = "Close!"
    elif distance <= 10:
        hint = "Not too far."
    else:
        hint = "Far away."

    if guess < secret:
        direction = "higher"
    else:
        direction = "lower"

    print(f"Wrong! Try {direction}. {hint}")
    print(f"Lives: {hearts}")

if attempts == 0 and guess != secret:
    print(f"Game over. The secret number was {secret}.")
