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

number_guesser()
    
    

    
