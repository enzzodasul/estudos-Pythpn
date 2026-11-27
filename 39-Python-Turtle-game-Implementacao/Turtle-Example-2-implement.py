
from turtle import *

# Configuração / Settings
move_distance = 20

screen = Screen()
screen.bgcolor("#D2691E")
screen.title("TURTLE GAME")

# Desenhar o mar / Draw the sea
penup()
goto(100, 200)
pendown()

color("blue")
begin_fill()

goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)

end_fill()

# Criar tartaruga / Create turtle
penup()
goto(-200, 0)

shape("turtle")
color("green")

# Movimento para cima / Move up
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

# Movimento para baixo / Move down
def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

# Movimento para esquerda / Move left
def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

# Movimento para direita / Move right
def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

# Verificar objetivo / Check goal
def check_goal():
    if xcor() > 100:
        hideturtle()
        color("white")
        write(
            "YOU WIN!",
            align="center",
            font=("Arial", 30, "bold")
        )

        screen.onkey(None, "Up")
        screen.onkey(None, "Down")
        screen.onkey(None, "Right")
        screen.onkey(None, "Left")

# Configurar controles / Set controls
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")

# Ativar teclado / Enable keyboard
screen.listen()

done()
