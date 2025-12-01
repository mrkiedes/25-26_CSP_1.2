# Import Turtle
import turtle as trtl

# Make a turtle
james = trtl.Turtle()

def drawSquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)

# Goal: to draw squares with a turtle

drawSquare()
james.forward(60)
drawSquare()





wn = trtl.Screen()
wn.mainloop()
