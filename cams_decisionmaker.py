#	 	   RANDOM NUMBER GENERATOR
# ---------------------------------------
# THIS PROGRAM WILL MAKE DECISIONS EASIER
import random

print("Welcome to Cam's Decision-Maker 3000")
print("\n")
print("How many decisons  are you faced with right now?")
choices = input("\tEnter:\t")
choices = int(choices)
#creation of empty array
list=[]
count = 1		
print("Enter choices one-by-one")
for i in range(choices):
	print ("%r :" %count)
	user_input = input("\t")
	count+=1
	list.append(user_input), i
print("Your randomly generated life-decison:")
#goes through list and randomly chooses an element
print(random.choice(list))
