from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False
i = 0
y_coor = -100
for i in range(3):
    n_turt = Turtle(shape="turtle")
    n_turt.penup()
    n_turt.color(colors[i])
    n_turt.goto(x=-230, y=y_coor)
    all_turtles.append(n_turt)
    y_coor +=30
    i+=1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

my_screen.exitonclick()