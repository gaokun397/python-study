#!/usr/bin/env python

import random
number = random.randint(0,100)

print "Hello,Number guessing Game: betwween 0 and 100 inclusive."

guessString = raw_input("guess a number: ")
guess = int(guessString)

while 0 <= guess <= 100:
    if guess > number:
        print "Guessed Too High,please guess again!."
    elif guess < number:
        print "Guessed Too Low,please guess again!."
    else:
        print "You guessed it. The number was:",number
        break
    guessString = raw_input("Guess a number: ")
    guess = int(guessString)
else:
    print "Your guess was not between 0 and 100,the game is over,the number was:",number
