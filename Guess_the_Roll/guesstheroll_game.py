import random
import os
import time

attempt= 0
def rollDice():
    valueroll= random.randint(1,6)
    print("The DICE roll is: ", valueroll)
    return valueroll

def clean():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

player= input("\nEnter your name: ")
clean()
print("* / * / * Loading * / * / *")
time.sleep(2)
clean()

print("Welcome!", player)
while True:
    roll=  input("\nEnter number between 1-6: ")
    roll= int(roll)
    valueroll= rollDice()
    if roll == valueroll:
        print(f"You have rolled the entered the correct number!\nAfter {attempt+1} attempts")
        break
    else:
        print("You LOST!")
        attempt+=1