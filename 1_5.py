import turtle
import random

def draw_branch(t, branch_length):
    if branch_length > 5:
        # Random angle and reduction for branches
        angle = random.randint(15, 45)
        reduction = random.randint(10, 20)

        t.width(branch_length / 8)

        # Move the turtle forward
        t.forward(branch_length)
        
        # Draw the right branch
        t.right(angle)
        draw_branch(t, branch_length - reduction)
        
        # Draw the left branch
        t.left(angle * 2)
        draw_branch(t, branch_length - reduction)
        
        # Return to the original position and heading
        t.right(angle)
        t.backward(branch_length)
    else:
        # Draw a leaf with random color
        t.color(random.choice(["green", "yellow", "red"]))
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color("brown")

def draw_fractal_tree():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    t = turtle.Turtle()
    t.color("brown")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    draw_branch(t, 100)
    window.mainloop()

draw_fractal_tree()
