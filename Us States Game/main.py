import turtle, pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Games")
image ="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 State Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missing.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data.state.item())


# data_list = data.values.tolist()
# stati = 50
#
# while stati != 0:
#     for elem in data_list:
#         if answer_state.lower() == elem[0].lower():
#             stati -= 1
#             x_coor = elem[1]
#             y_coor = elem[2]
#             new_state = Turtle()
#             new_state.color("black")
#             new_state.hideturtle()
#             new_state.penup()
#             new_state.goto(x=x_coor, y=y_coor)
#             new_state.write(answer_state, align="center", font=("Arial", 10, "normal"))
#             break
#     answer_state = screen.textinput(title=f"{stati}/50 Guess the State", prompt="What's another state's name?")


#turtle.mainloop()