import random
import time

def display_intro():
    print('''
    You are in a land full of dragons.In front of you,
    you see two caves. In one cave, the dragon is friendly 
    and will share his treasure with you. The other dragon 
    is greedy and hungry, and will eat you on sight.
    ''')
    print()

def choose_cave():
    cave= ''
    while cave!='1' or cave!='2':
        cave= input("which cave will yougo into? (1 or 2)\n")
        return cave

def check_cave(choose_cave):
    print("you approach the cave...")
    time.sleep(2)
    print("it is dark and spooky")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)
    safe_cave= random.randint(1,2)
    if safe_cave==choose_cave:
        print("gives you his treasure!")
    else:
        print("gobbles you down in one bite")

play_again= 'yes'
while play_again=='yes':
    display_intro()
    cave= choose_cave()
    check_cave(cave)
    play_again=input("do you want to play again?\n")