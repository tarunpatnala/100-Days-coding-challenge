import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# def get_mouse_click_corr(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_corr)
#
# turtle.mainloop()

states = pandas.read_csv("50_states.csv")
all_states = states["state"].to_list()
turtle2 = turtle.Turtle()
turtle2.penup()
turtle2.color("black")
turtle2.hideturtle()
guessed_states = []
count = 0
game_is_on = True
while len(guessed_states) < 50:
    result = screen.textinput(f"{count}/50 States Correct", "What's another state name?").title()
    if result == "Exit":
        break
    if result in all_states:
        guessed_states.append(result)
        count += 1
        state_data = states[states.state == result]
        turtle2.goto(int(state_data.x), int(state_data.y))
        turtle2.write(result)

not_guessed_state = []
for item in all_states:
    if item not in guessed_states:
        not_guessed_state.append(item)

data = pandas.DataFrame(not_guessed_state)
data.to_csv("not_guessed_states.csv", index=False, header=False)
