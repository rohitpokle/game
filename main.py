import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='p':
            return False
        elif you=='x':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'p':
        if you=='x':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'x':
        if you=='s':
            return False
        elif you=='p':
            return True

print("Comp Turn: stone(s) paper(p) or cezer(x)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'x'

you = input("Your Turn: stone(s) paper(p) or cezer(x)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")