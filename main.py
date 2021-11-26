import random
import turtle

turtle.colormode(255)


def generate_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


my_turtle = turtle.Turtle()
screen = turtle.Screen()
my_turtle.shape("turtle")

my_turtle.penup()
x_position = -310
y_position = -260
my_turtle.setx(x_position)
my_turtle.sety(y_position)


def draw_dots():
    for _ in range(12):
        my_turtle.dot(20, generate_color())
        my_turtle.penup()
        my_turtle.forward(55)
        my_turtle.pendown()


def change_position():
    global y_position
    y_position += 40
    my_turtle.penup()
    my_turtle.setx(x_position)
    my_turtle.sety(y_position)
    my_turtle.pendown()


for _ in range(14):
    draw_dots()
    change_position()

screen.exitonclick()
