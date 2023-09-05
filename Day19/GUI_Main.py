from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.setheading(180)
    tom.forward(10)


def move_counter_clickwise():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def move_clockwise():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clickwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
