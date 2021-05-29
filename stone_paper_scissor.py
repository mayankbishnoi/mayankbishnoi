import time
import random

def comparing_both(comp, you):
#Set the value when comp = you
    if comp == you:
        return None

#Set the value when comp chooses stone

    elif comp == "stone":
        if you == "paper":
            return True
        elif you == "scissor":
            return False
# Set the value when comp chooses paper
    elif comp == "paper":
        if you == "stone":
            return False
        elif you == "scissor":
            return True
# Set the value when comp chooses scissor
    elif comp == "scissor":
        if you == "stone":
            return True
        elif you == "paper":
            return False
def winGame():
    a = comparing_both(comp, you)
    if a is True:
        print("You won!!")
    elif a is None:
        print("The game is tied....")
    elif a is False:
        print("OOPs!!! You Loose.....")        

while winGame:
    c = 3
    time.sleep(c)
    print("Computer's turn: Stone| Paper| Scissor ")
    rand_no = random.randint(1,3)
    if rand_no == 1:
        comp = "stone"
    elif rand_no == 2:
        comp = "paper"
    elif rand_no == 3:
        comp = "scissor"


    you = int(input("your turn: Stone| Paper| Scissor>> \
\ntype '1' for Stone \
\ntype '2' for Paper \
\ntype '3' for Scissor \
>>"))
    if you == 1:
        you = "stone"
    elif you == 2:
        you = "paper"
    elif you == 3:
        you = "scissor"

    print(f"You choose {you}")
    print(f"The computer choose ",comp)
    t = 3
    time.sleep(t)
    winGame()
