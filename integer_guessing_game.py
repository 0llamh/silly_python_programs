#Cameron Smith
#integer guessing game

from random import randint
from time import sleep
#this allows for delayed print using a sleep method
import sys
sys.stdout.flush()
sleep(0.1)

def print_delay(line):
	for character in line:
		print(character, end='')
		sys.stdout.flush()
		sleep(0.075)
#goes through each character in a string and pauses
#before printing to console like someone is typing
		
integer_to_guess = randint(1,100)
		
print_delay("Let us play a little game...\n")
sleep(0.5) #longer pause after a line.
#adds suspense
print_delay("...a guessing game.\n")
sleep(0.5)
print_delay("I want you to guess what number I am thinking of between 1 and 100.\n")
sleep(0.5)
print_delay("Go ahead. ")
sleep(0.5)
print_delay("Try.\n")
sleep(0.5)
print('\n')

while True:
	#do-while loop
	guess = input()
	guess = int (guess)
	if guess == integer_to_guess:
		print("Correct. You win this time...")
		break
	elif guess < integer_to_guess:
		print("Higher.")
	elif guess > integer_to_guess:
		print("Lower.")
	else
		print("You don't make any sense, human.")