from turtle import Screen, Turtle
from scoreboard import Scoreboard
from turntext import TurnText
import time
import random

CURSOR_SIZE = 20
FONT_SIZE = 12
is_on = True
FONT = ('Arial', FONT_SIZE, 'bold')

scoreboard = Scoreboard()
turntext = TurnText()

Player = Turtle(shape="turtle")
Player.color("purple")
Player.penup()
Player.goto(x=-250, y=-20)

Ai = Turtle(shape="turtle")
Ai.color("orange")
Ai.penup()
Ai.goto(x=-250, y=-100)

screen = Screen()
screen.addshape('zebra_crossing_6.gif')

zebra = Turtle()
zebra.shape('zebra_crossing_6.gif')
zebra.penup()
zebra.goto(300, -45)


def draw_onclick(x, y):
    if turntext.turn == "Your turn":
        rand_dist1 = random.randint(1, 6)
        dicetext1 = Turtle()
        dicetext1.penup()
        dicetext1.goto(0, 80)
        dicetext1.hideturtle()
        dicetext1.write(rand_dist1, align="center", font=('Arial', 12, 'bold'))
        Player.forward(rand_dist1*25)
        time.sleep(1)
        dicetext1.clear()
        turntext.r_point()
        """Ai's turn"""
        rand_dist2 = random.randint(1, 6)
        dicetext1 = Turtle()
        dicetext1.penup()
        dicetext1.goto(0, 80)
        dicetext1.hideturtle()
        dicetext1.write(rand_dist2, align="center", font=('Arial', 12, 'bold'))
        Ai.forward(rand_dist2*25)
        time.sleep(1)
        dicetext1.clear()
        turntext.l_point()


button = Turtle()
button.hideturtle()
button.shape('circle')
button.fillcolor('red')
button.penup()
# button.goto(0, 100)
# button.write("click me!", align='center', font=FONT)
button.sety(100 + CURSOR_SIZE + FONT_SIZE)
button.onclick(draw_onclick)
button.showturtle()

turtle = Turtle()
turtle.hideturtle()

tut_list = [Player, Ai]

while is_on:
    for turtle in tut_list:
        if turtle.xcor() >= 250:
            is_race_on = False
            winning_turtle = tut_list.index(turtle)
            if winning_turtle == 0:
                print(f"You win!!!")
            else:
                print(f"You loose:(")

# if not is_on:
#     screen.exitonclick()

screen.mainloop()