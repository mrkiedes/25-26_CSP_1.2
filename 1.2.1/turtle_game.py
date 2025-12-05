#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
score_writer = trtl.Turtle()
score_writer.penup()

meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    score_writer.goto(275, 325)
    score_writer.pendown()

    # Draw the box
    for sides in range(2):
        score_writer.forward(100)
        score_writer.left(90)
        score_writer.forward(50)
        score_writer.left(90)

    # Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 325)

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    meowl.goto(newX, newY)
    update_score()

def update_score():
    # Include the global score
    global score
    # Increment the score by 1
    score += 1
    # print the score
    score_writer.write(score, font=font_setup)

#-----events----------------
meowl.onclick(spot_clicked)

scoreBox()
wn = trtl.Screen()
wn.mainloop()