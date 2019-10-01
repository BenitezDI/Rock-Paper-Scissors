#Dayanara Benitez
#September 30
#period 6
#Rock,Paper,Scissors 
#comment here 
import random

#Varibles
pScore = 0
cScore = 0 
ties = 0
cMoves = [ "rock", "paper", "scissors" ]


#Welcome Message 
#print welcome message 
print("Welcome to Rock,Paper,Scissors")
#prompt for name 
pName= input("What is your name? ")

# Score Tracker 
# Make a function
def printScore():

	# Print Score
	print("Score: ")
# Shows player Score
	print(pName + ": " + str(pScore))
# Shows the coputers score
	print("Computer Score: " + str(cScore))
# Shows how many ties 
	print("Ties: " + str(ties))
# Game Loop
# Loop until q is entered
while True: 
# Prompt for player move (r,p.s.q)
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors, or 'q' to Quit")
# Print the score 
	printScore()

# Check if q is entered if so end the game 
	if pMove == 'q':
		break
# Get a computer move (random) 
	cMove = random.choice(cMoves)
#Compare player move with computer move 
# Player picks rock
	if pMove == "r":
		print(pName + "picked  Rock")
		if cMove == "rock":
			print("Computer picks Rock")
			print("Tie")
			ties += 1 
		elif cMove == "paper":
			print("Computer picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else:
			print("Computer picks Scissors")
			print("Rock breaks scissors")
			cScore += 1
# Player picks paper
	elif pMove == "p":
		pass
# Player picks scissors 
	elif pMove == "s":
		pass
# Check is pMove is valid
	else: 
		print("That is not an option")