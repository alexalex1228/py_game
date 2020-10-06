import random

guessesTaken= 0

print("hello! what is your name? ")
#input the user name
name= input()
print("Well," +  name + ", I am thinking a number between 1 and 20")
number= random.randint(1,20)
for i in range(6):
    print("Take a guess:")
    guess= input()
    guess= int(guess)
    guessesTaken= guessesTaken+1

    if guess<number:
        print("Your guess is too low")
    if guess>number:
        print("Your guess is too high")
    if guess==number:
        break

#print the result
if guess==number:
    guessesTaken= str(guessesTaken)
    print("Good job "+name+"! You gueessed my number in "+guessesTaken+" guesses!")
else:
    number= str(number)
    print("Nope. The number I was thinking is "+number+".")