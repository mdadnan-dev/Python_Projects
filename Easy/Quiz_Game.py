print("Welcome to a General Knowledge Quiz !")

playing = input("Would you like to play ?  ")

if playing.lower() != 'yes':
    quit()

print("Let's get started!")
score = 0


answer = input("Which data structure follows LIFO principle ?  ")

if answer == 'Stack':
    print("Correct !")
    score += 1
elif answer == 'stack':
    print("Correct !")
    score += 1
else:
    print("Incorrect !")


answer = input("Which numpy function is used to create an array of zeros ?  ")

if answer.lower() == 'np.zeros()':
    print("Correct !")
    score += 1
else:
    print("Incorrect !")


answer = input("What is the chemical symbol for gold ?  ")

if answer == 'Au':
    print("Correct !")
    score += 1
else:
    print("Incorrect !")


answer = input("What is the capital of Japan ?  ")

if answer.capitalize() == 'Tokyo':
    print("Correct !")
    score += 1
else:
    print("Incorrect !")

print("You got " + str(score) + " questions correct")
print("Your Final Score is -",(score / 4) * 100, '%')
