from ast import While
import random


while True:

    choices = ['r', 'p', 's']
    com = random.choice(choices) #computers choices
    user = input("Choose between r (for rock ), p (for paper) and s (scissors): ") #user choice

    def result() : print ({"COM": com, "User": user})

    if user == "":
        print('Please input a choice between r, p or s')
    elif user == com:
        result()
        print ('Tie')
        continue

    elif user == 'r':
        result()
        user_fate = 'Win' if com == 'p' else 'Lose'
        print (user_fate)

    elif user == 'p':
        result()
        user_fate = 'Win' if com == 's' else 'Lose'
        print (user_fate)

    elif user == 's':
        result()
        user_fate = 'Win' if com == 'r' else 'Lose'
        print (user_fate)
    
    elif user!= 'r' or 'p' or 's':
        print ( "Error: Invalid input! Choose between rock, paper & scissors " )
        continue

    user = input ('Play Again? y/n: ')
    while True:
        if user == "n":
            break
        if user == "y":
            continue
        elif user != "y" or user != "n" :
            print ("Invalid input! input 'y' for yes and 'n' for no")
            input ('Play Again? y/n: ')