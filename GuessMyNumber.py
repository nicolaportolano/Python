# The program generates a random integer from 1 to 10 and asks the user to guess it. The user can then enter a number and the program
# will give hints to whether the number entered is too high or to low. At every stage of the game the program checks that that the user
# inputs an allowed value. The player can exit at any time by typing 'exit'. At the end of the game, the program will 
# ask the user if he/she wants to play again by typing 'yes' or 'no'. 

from random import randint
import sys
import re
tot = 0

def game():

        def playagain():
                
                """ASKS IF PLAYER WANTS TO PLAY AGAIN"""

                again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
                if again == 'yes':
                        game()
                if again == 'no':
                        print ('\nOk, bye bye!\n\n')
                        sys.exit()
                else:
                        print ("\nplease type either 'yes' or 'no'!")
                        playagain()
        
        def checkType(x):
                
                """CHECKS THAT USER INPUTS ONLY ALLOWED VALUES"""
                
                if x == 'exit':
                        print ('\nOk, bye bye!\n\n')
                        sys.exit()
                else:
                        if contains_alphas(x) or x == "":
                                x = input("\nThis is not a number!\nTry to guess my number from 1 to 10 or type 'exit' to quit. ")
                                checkType(x)
                        else:
                                guessNum(x)
                               
        def guessNum(n):
                global tot
                
                """HELPS THE USER GUESS THE NUMBER; CALLS playagain() IF USER WINS;
                CALLS checkType IF USER INPUTS AN NON PERMITTED VALUE"""

                if int(n) == x:
                        print ('\nYou win!! You guessed after %s attempts!'%tot)
                        tot = 0
                        playagain()

                while int(n) > x:
                        n = input('\nTry a smaller number: ')
                        
                        if n == 'exit':
                                print ('\nOk, bye bye!\n\n')
                                sys.exit()
                                
                        if contains_alphas(n) or n == "":
                                checkType(n)
                        
                        else:
                                tot += 1
                                guessNum(n)
        
                while int(n) < x:
                        n = input('\nTry a bigger number: ')
                        if n == 'exit':
                                print ('\nOk, bye bye!\n\n')
                                sys.exit()
                        if contains_alphas(n) or n == "":
                                checkType(n)
                        else:
                                tot += 1
                                guessNum(n)
                                
        
        
        x = randint(1,10)
                                
        guess = input("\n\nTry to guess my number from 1 to 10 or type 'exit' to quit. ")

                
        def contains_alphas(a):
                alp = re.compile('\D')
                return bool(alp.search(a))
        
        
        checkType(guess)
                        
game()

 


                        
                
