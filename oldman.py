import turtle
import time

screen = turtle.Screen()
screen.title("Oldman Image by Vybekid/CRyptofelo")
screen.setup(width=500, height=500)

screen.tracer(0)

image_filename = "0.gif" 

# --- Sequence Start ---

# Stage 1: Display an empty screen for 4 seconds
# ------------------------------------------------
# We manually update the screen once to make sure the empty window is visible.
screen.update()
time.sleep(4)

# Stage 2: Display the image for 4 seconds
# ------------------------------------------
# Register the shape and create the turtle for the image.
screen.addshape(image_filename)
image_turtle = turtle.Turtle()
image_turtle.shape(image_filename)
# Now, update the screen to show the image.
screen.update()
time.sleep(4)

# Stage 3: Add the caption
# -------------------------
# Create the writer turtle and write the text.
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
y_position = screen.window_height() / 2 - 40
writer.goto(0, y_position)
writer.write(
    "Subscribe to Vybekid",
    align="center",
    font=("Arial", 18, "bold")
)
# Finally, update the screen one last time to show the caption.
screen.update()

# Keep the final result visible until the user clicks
screen.exitonclick()