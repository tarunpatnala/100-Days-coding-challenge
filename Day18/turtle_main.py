import random
from turtle import Turtle, Screen, colormode

timmy = Turtle()
timmy.shape("circle")

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)
colors = ["Cornflowerblue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for i in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(i)
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


#
# directions = [0, 90, 180, 270]
# timmy.pensize(15)
# timmy.speed("fastest")
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
