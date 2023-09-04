# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import random
import turtle as t
tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
rgb_colors = [(233, 233, 232), (226, 231, 238), (223, 233, 226), (238, 229, 233), (206, 161, 88), (55, 88, 129), (146, 91, 41), (139, 26, 50), (221, 206, 106), (134, 175, 201), (155, 49, 83), (45, 55, 102), (167, 158, 40), (129, 188, 144), (82, 20, 43), (37, 42, 68), (185, 93, 107), (186, 141, 170), (86, 118, 178), (58, 39, 29), (87, 156, 92), (78, 153, 163), (193, 80, 73), (79, 74, 43), (60, 123, 114), (45, 74, 78), (162, 201, 217), (220, 175, 188), (45, 76, 75), (169, 207, 169)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100
for i in range(1, numbers_of_dots +1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
