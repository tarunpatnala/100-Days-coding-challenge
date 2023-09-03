# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.turtlesize(1)
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Test", ["1", "2", "3"])
table.add_column("Type", ["X", "Y", "Z"])
print(table)