import random

first_name = ['Albie', 'Biff', 'Chug', 'Doodle', 'Eggbert', 'Fizzle', 'Goober', 
              'Hootie', 'Itchy', 'Jibby', 'Klunk', 'Lumpy', 'Mungo', 'Niblet', 
              'Ozzie', 'Pogo', 'Quackers', 'Rufus','Snerd', 'Tater']

last_name = ['Bumblesnatch', 'Dingleberry', 'Flapdoodle', 'Giggletush', 'Hootenanny', 
             'Jigglepants', 'Kazoozle', 'Loofahsniff', 'McSqueaky', 'Noodlekins', 
             'Oinkmeister', 'Puddingpop', 'Quackington', 'Rufflebottom', 'Snickersnee',
             'Taterchunks', 'Umperdink', 'Wobblecheeks', 'Yodelstein', 'Zippitydoo']

while True:
    answer = input("Press 'ok' to generate a Funny Name or else 'q' to quit - ").lower()
    random_number = random.randint(0,19)
    random_Name = first_name[random_number] + ' ' + last_name[random_number]
    if answer == 'q':
        break
    else:
        print(random_Name)
        continue

print("Thank You for playing") 

