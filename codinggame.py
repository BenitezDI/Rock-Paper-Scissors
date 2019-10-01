import random 

mysteryNum = random. randint(1,100)
score = 0

while True:
	guess = int(input("Guess a number between 1 and 100: "))
	score += 1
	if guess == mysteryNum:
		print ("You have guessed correctly, good job!!")
		break 
	elif guess > mysteryNum:
		print("Too High, try again")
	else: 
		print("Too Low, try again")

print("You took " + str(score) + "guess")