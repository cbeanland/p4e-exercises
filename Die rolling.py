#Dice simulator with 2 die giving a total between 2 and 12. The use can choose to play with only 1 dice

import random

result1 = 0
result2 = 0
game = True

def single_die():
    result = random.randint(1,6)
    return result

tmp = input("how many die do you want to play with: ",)
no_of_die = int(tmp)

if (no_of_die < 1) or (no_of_die > 2):
    print("we can only work with 1 or 2 die right now im afraid")
else:
    while (game == True):
        rollchoice = input("do you want to roll? ",)
        if (rollchoice == "yes"):
            if (no_of_die == 1):
                result1 = single_die()
                print(result1)
            elif (no_of_die == 2):
                result2 = single_die() + single_die()
                print(result2)
        elif (rollchoice == "no"):
            game = False
        else:
            print("sorry i didnt recognise that, please try again")
 
