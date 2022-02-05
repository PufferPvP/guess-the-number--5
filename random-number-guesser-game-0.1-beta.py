# random number guesser game
from asyncore import loop
from lib2to3.pgen2.token import GREATER, GREATEREQUAL, LESS, LESSEQUAL
from operator import countOf
import random
from tracemalloc import stop
flag = True
while flag:
    num = input('Type a number for an upper bound:  ')
    if num.isdigit() :
        print("let's play!")
        num = int(num)
        flag = False
        secret = random.randint(1,num)
        guess = None
        count = 0
        while guess != secret:
            guess = input("Please type a number between 1 and" + str(num) + ": ")
            if guess.isdigit() :
                guess = int(guess)
                count=count+1
                if guess > secret:
                    print("too high")
                elif guess < secret:
                    print("too low")
                elif guess == secret:
                    print("It took you", count, "guesses")
                    
                    print("You got it right!")                                                 
                else:
                      
                    print("Please try again!")
                    
    