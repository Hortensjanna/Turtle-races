
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("TURTLE RACES")
screen.bgcolor('black')
user_bet = screen.textinput(title='Make your bet', prompt='            Which turtle will win the race? '
                                                          '\n(red/ orange/ yellow/ green/ blue/ purple) '
                                                          '\n                        Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

finish_turtles = []

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230 and turtle.pencolor() not in finish_turtles:
            finish_turtles.append(turtle.pencolor())
        if len(finish_turtles) == 3:
            is_race_on = False

else:
    winning_color = finish_turtles[0]
    second_place = finish_turtles[1]
    third_place = finish_turtles[2]
    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner! "
              f"The {second_place} turtle is in the second place and {third_place} turtle is in the third place.")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner! "
              f"The {second_place} turtle is in the second place and {third_place} turtle is in the third place.")


screen.exitonclick()
