import random

user_score = 0
computer_score = 0

options = ['rock','paper','scissors']

while True:
    user_input = input("Type rock/paper/scissors or q to quit: ").lower()

    if user_input == 'q':
        break
    elif user_input not in options:
        continue

    random_number = random.randint(0,2) # 0-> rock, 1-> paper, 2->scissors
    computer_choice = options[random_number]
    print("Computer picked :",computer_choice)
    print("User picked :",user_input)

    if user_input == 'rock' and computer_choice == 'scissors':
        print("You won")
        user_score += 1

    elif user_input == 'scissors' and computer_choice == 'paper':
        print("You won")
        user_score += 1
    
    elif user_input == 'paper' and computer_choice == 'rock':
        print('You won')
        user_score += 1

    elif user_input == 'rock' and computer_choice == 'rock':
        print("It's a Draw")

    elif user_input == 'scissors' and computer_choice == 'scissors':
        print("It's a draw")
        
    elif user_input == 'paper' and computer_choice == 'paper':
        print("It's a draw")

    else:
        print("Computer won")
        computer_score += 1

print("Your Score is",user_score)
print("Computer Score is",computer_score)

if user_score > computer_score:
    print("User Won")
    print("Congrats")
elif user_score < computer_score:
    print("You Lost")
    print("Better Luck Next Time")
else:
    print("It's a draw.")

print("Goodbye")