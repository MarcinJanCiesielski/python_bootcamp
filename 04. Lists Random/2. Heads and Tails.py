#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

coin = random.random()

if coin < 0.5:
    print("Tails")
else:
    print("Heads")
