"""
Reference: http://blog.tibarazmi.com/draw-flower-using-turtle/

You can use https://trinket.io/python if you have problem running turtle
"""
import turtle
import math


def p_line(t, n, length, angle):
    """Draws n line segments."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides."""
    angle = 360 / n
    p_line(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # Before starting reduces, making a slight left turn.
    t.lt(step_angle / 2)
    p_line(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def petal(t, r, angle):
    """Draws a petal using two arcs."""
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, n, r, angle, p):
    """Draws a flower with n petals."""
    for i in range(n):
        petal(t, r, angle)
        t.lt(p / n)


def leaf(t, r, angle, p):
    """Draws a leaf and fill it."""
    t.begin_fill()  # Begin the fill process.
    t.down()
    flower(t, 1, 40, 80, 180)
    t.end_fill()


def main():
    window = turtle.Screen()  # creat a screen
    window.bgcolor("blue")
    lucy = turtle.Turtle()
    lucy.shape("turtle")
    lucy.color("red")
    lucy.width(5)
    lucy.speed(0)

    # Drawing flower
    flower(lucy, 10, 40, 100, 360)

    # Drawing pedicel
    lucy.color("brown")
    lucy.rt(90)
    lucy.fd(200)

    # Drawing leaf
    lucy.rt(270)
    lucy.color("green")
    leaf(lucy, 40, 80, 180)
    lucy.ht()
    window.exitonclick()

# call the main function to start!
main()