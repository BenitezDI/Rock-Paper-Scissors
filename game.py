from turtle import *

scoreTurtle = Turtle()
myScreen = scoreTurtle.getscreen()
scoreTurtle.penup()
scoreTurtle.goto(mySrceen.window_width() / 2 + 200, myScreen.window_width()/2-50)
scroreTurtle. hideturtle()
score = 0

def updateScore():
	scoreTurtle.clear()
	scroreTurtle.write("Score: " + str(score), False, "left", font=("Arial", 20, "normal"))

updateScore()

myScreen.mainloop()