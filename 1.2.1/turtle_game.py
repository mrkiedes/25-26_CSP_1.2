#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
# Score turtle
score_writer = trtl.Turtle()
score_writer.penup()
counter =  trtl.Turtle()
counter.penup()

# Turtle to draw a box
box_turtle = trtl.Turtle()
box_turtle.penup()

# Shape turtle
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    # Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    # Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 332)

    # Hide the turtles
    score_writer.hideturtle()
    box_turtle.hideturtle()

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
    else:
        meowl.hideturtle()

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
    # Clear out the prior score
    score_writer.clear()
    # Print the current score
    score_writer.write(score, font=font_setup)

# Counter setup
def counter_setup():
    counter.forward(-200)
    counter.left(90)
    counter.forward(300)
    counter.right(90)
    counter.hideturtle()

# Start the countown and update it each frame
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
#-----events----------------
meowl.onclick(spot_clicked)
counter_setup()
scoreBox()
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()