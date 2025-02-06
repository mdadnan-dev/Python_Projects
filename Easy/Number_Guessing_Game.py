import random


top_range = input("Enter a number [It will be considered as the maximum value of a range] -  ")

if top_range.isdigit():
    top_range = int(top_range)
    
    if top_range <= 0:
        print("Enter a larger number greater than 0  next time ! ")
        quit()

else:
    print("Enter a number next time ! ")
    quit()

random_number = random.randint(0, top_range)

print("Guess a number between (0-" + str(top_range)+')')

guesses = 0

while True:
    guesses += 1
    guess_number = input("Make a guess - ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Enter a number next time")
        continue
    
    if guess_number == random_number:
        print("You got it")
        break
    elif guess_number > random_number:
        print("You are above the number")
    else:
        print("You are below the number")
       

print("You found the number in ",guesses,'guesses.')
