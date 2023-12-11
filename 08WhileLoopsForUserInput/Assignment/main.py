import random
def number_guesser():
    secret_number = random.randint(1, 10)
    guess = ""
    while guess != secret_number:
        print("Type a random number between 1 and 10!")
        guess = int(input())
        
        if guess == secret_number:
            print("Good Job!")
        elif guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")

# number_guesser()

import random
def number_guesser_with_lives():
    secret_number = random.randint(1, 10)
    guess = ""
    lives = int(3)

    while guess != secret_number and lives > 0:
        print("Type a random number between 1 and 10! Be careful!")
        guess = int(input())
        
        if guess > secret_number:
            lives = lives - 1
            print("Too high!", lives, "lives left")
        elif guess < secret_number:
            lives = lives - 1
            print("Too low!", lives, "lives left")
        elif guess == secret_number:
            print("Good Job!", lives, "lives left")
        
        if lives == 0:
            print("No more lives remaining. Better luck next time!")
            print("The secret number was:", secret_number)

# number_guesser_with_lives()

def vending_machine():
    cost = 50
    paid = 0

    while paid != cost:
        print("Your snack costs", cost - paid, "cents. What is the amount you will pay? (Courters, dimes, or nickels only)")
        amount = int(input())
        paid = paid + amount

        if amount == 25 or amount == 10 or amount == 5:
            print("You owe", cost - paid, "more cents.")
        
        if paid == 50:
            print("You paid for your snack! Hope you like it!")

vending_machine()


    

    
