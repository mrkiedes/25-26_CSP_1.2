# Import Turtle
import turtle as trtl

# Make a turtle
james = trtl.Turtle()

def drawSquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)

# Goal: to draw squares with a turtle

drawSquare(62)
james.forward(100)
drawSquare(47)





wn = trtl.Screen()
wn.mainloop()
