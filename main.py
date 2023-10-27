import random
#basically its an application of binary search
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number: 
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess > random_number:
            print("Sorry, guess again. Too high.")
        elif guess < random_number:
            print ("Sorry, guess again. Too low")
    
    print(f"Yay! congrats! Yu have guessed the number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c': 
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too high(c) or too low(l) or correct(c)').lower()
        if feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess -1
        
    print(f'Yay! computer guessed your number {guess} correctly')


# guess(10)
computer_guess(100)