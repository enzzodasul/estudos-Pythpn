
# ============================================================
# TURTLE GAME - PRAIA E MAR
# TURTLE GAME - BEACH AND SEA
#
# Objetivo: levar a tartaruga da praia até o mar.
# Goal: move the turtle from the beach to the sea.
#
# Controles / Controls:
# ↑ UP    = Cima / Up
# ↓ DOWN  = Baixo / Down
# ← LEFT  = Esquerda / Left
# → RIGHT = Direita / Right
# ============================================================

import turtle

# ============================================================
# 1. CONFIGURAÇÕES DA TELA / SCREEN SETTINGS
# ============================================================

screen = turtle.Screen()

screen.title("TURTLE GAME - Beach Adventure")
screen.setup(width=900, height=600)
screen.bgcolor("#F4F4F4")
screen.tracer(0)

# ============================================================
# 2. CRIAR O CENÁRIO / CREATE THE SCENERY
# ============================================================

def draw_rectangle(pen, x, y, width, height, color):
    """Desenha um retângulo / Draws a rectangle."""

    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.begin_fill()
    pen.pendown()

    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    pen.end_fill()
    pen.penup()


background = turtle.Turtle()
background.hideturtle()
background.speed(0)

# Praia / Beach
draw_rectangle(
    background,
    -430, -250,
    500, 500,
    "#FF8733"
)

# Mar / Sea
draw_rectangle(
    background,
    70, -250,
    360, 500,
    "#079ED8"
)

# Linha da costa / Shoreline
background.penup()
background.goto(70, -250)
background.color("#FFF1C1")
background.pensize(5)
background.pendown()
background.goto(70, 250)
background.penup()

# Ondas do mar / Ocean waves
background.color("#8CE5FF")
background.pensize(3)

for y in range(-200, 250, 65):
    background.goto(110, y)
    background.pendown()

    for x in range(110, 400, 12):
        wave_y = y + (8 if (x // 12) % 2 == 0 else -8)
        background.goto(x, wave_y)

    background.penup()

# Texto da praia / Beach label
background.goto(-250, 190)
background.color("#FFFFFF")
background.write(
    "BEACH",
    align="center",
    font=("Arial", 25, "bold")
)

# Texto do mar / Sea label
background.goto(250, 190)
background.write(
    "SEA",
    align="center",
    font=("Arial", 25, "bold")
)

# ============================================================
# 3. OBJETIVO FINAL / FINAL DESTINATION
# ============================================================

goal = turtle.Turtle()
goal.hideturtle()
goal.penup()

# Desenhar círculo de chegada / Draw finish circle
goal.goto(300, 0)
goal.color("#FFFFFF")
goal.dot(85)

goal.goto(300, 0)
goal.color("#FFD700")
goal.dot(65)

goal.goto(300, -8)
goal.color("#17324D")
goal.write(
    "FINISH",
    align="center",
    font=("Arial", 11, "bold")
)

# ============================================================
# 4. CRIAR A TARTARUGA / CREATE THE TURTLE
# ============================================================

player = turtle.Turtle()

player.shape("turtle")
player.color("#00A85A")
player.shapesize(2)
player.penup()

# Posição inicial na praia / Starting position on the beach
player.goto(-300, 0)
player.setheading(0)

# Velocidade de movimento / Movement speed
movement_speed = 20

# Estado do jogo / Game state
game_won = False

# ============================================================
# 5. FEEDBACK VISUAL / VISUAL FEEDBACK
# ============================================================

message = turtle.Turtle()
message.hideturtle()
message.penup()

def win_game():
    """Mostra a mensagem de vitória / Displays the victory message."""

    global game_won

    if game_won:
        return

    game_won = True

    message.goto(0, -15)
    message.color("#FFFFFF")

    message.write(
        "YOU WIN!",
        align="center",
        font=("Arial", 38, "bold")
    )

    message.goto(0, -65)
    message.color("#FFD700")

    message.write(
        "Congratulations! You reached the sea!",
        align="center",
        font=("Arial", 15, "bold")
    )

    screen.update()


# ============================================================
# 6. MOVIMENTAÇÃO / MOVEMENT
# ============================================================

def move_up():
    """Move a tartaruga para cima / Moves the turtle up."""

    if game_won:
        return

    player.setheading(90)
    player.sety(
        min(230, player.ycor() + movement_speed)
    )

    check_goal()
    screen.update()


def move_down():
    """Move a tartaruga para baixo / Moves the turtle down."""

    if game_won:
        return

    player.setheading(270)
    player.sety(
        max(-230, player.ycor() - movement_speed)
    )

    check_goal()
    screen.update()


def move_left():
    """Move a tartaruga para esquerda / Moves the turtle left."""

    if game_won:
        return

    player.setheading(180)
    player.setx(
        max(-410, player.xcor() - movement_speed)
    )

    check_goal()
    screen.update()


def move_right():
    """Move a tartaruga para direita / Moves the turtle right."""

    if game_won:
        return

    player.setheading(0)
    player.setx(
        min(410, player.xcor() + movement_speed)
    )

    check_goal()
    screen.update()


# ============================================================
# 7. VERIFICAR OBJETIVO / CHECK THE GOAL
# ============================================================

def check_goal():
    """Verifica se a tartaruga chegou ao mar.
    Checks whether the turtle has reached the sea."""

    if player.xcor() >= 260:
        win_game()


# ============================================================
# 8. CONFIGURAR TECLADO / KEYBOARD CONTROLS
# ============================================================

screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# ============================================================
# 9. INFORMAÇÕES NA TELA / SCREEN INSTRUCTIONS
# ============================================================

instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()

instructions.goto(0, -280)
instructions.color("#17324D")

instructions.write(
    "USE THE ARROW KEYS TO MOVE THE TURTLE",
    align="center",
    font=("Arial", 15, "bold")
)

# ============================================================
# 10. INICIAR JOGO / START GAME
# ============================================================

screen.update()

turtle.done()

