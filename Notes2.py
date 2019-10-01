# Conditional

print("Welcome to Ticket Box")
print("You must be at least 18 to see and R rated movies")
age = int(input("How old are you"))

if age > 17:
	print("You can go see an R rated movie")
else: 
	print("You cannot go see an R rated movie")

print("Thank you")

mysteryNum = 6 
guess = int(input("Guess a number between 1 and 10:"))

if guess == mysterNum:
	print ("Good Guess, this is correct")

elif guess > 10 
	print("Please read directions ")
elif guess > mysteryNum:
	print("Too High")

else 
	print("Too Low")

# conditional operators: >,<, >=,<=, == (is equal to), != ( is not equal to)

birthday = input("Is today your birthday(yes/no): ") 
if birthday == "yes":
	print ("Happy Birthday")
elif birthday == "no":
	print("Well have a good day anyways")
else: 
	print("Please read directions")