import random

x,y=map(int,input("Enter Low and High number with a space: ").split())

def comp_guess(x,y):
    
    low = x
    high = y
    feedback =''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess =low
        feedback = input(f"Is {guess} number too low(l) or too high(h) or correct(c)? ").lower()
        if feedback == 'l':
            low = guess +1
        elif feedback =='h':
            high = guess -1
    print(f"Yes {guess} is the correct answer!")    



def user_guess(x,y):
    random_num =random.randint(x,y)
    guess = 0
    count = 0

    while guess != random_num and count<5 :
        guess = int(input("Enter your guess: "))
        if guess > random_num:
            print(f"{guess} number is too high!")
            count +=1
        elif guess < random_num:
            print(f"{guess} number is too low!")
            count +=1
    if guess == random_num:
        print(f"Yes {guess} is the correct guess!")
    else :
        print("You lost the game! Sorry.")
user_guess(x,y)
