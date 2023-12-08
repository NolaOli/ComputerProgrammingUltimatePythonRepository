import random
def number_guesser(integer):
    if integer == random.randint(1,10):
        return "Good Job!"
    elif integer > random.randint(1,10):
        return "Too high"
    elif integer < random.randint(1,10):
        return "Too low"
    
