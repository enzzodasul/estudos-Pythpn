
# ============================================================
# BALLOON POPPER - INTERACTIVE GAME
# JOGO INTERATIVO DE ESTOURAR BALÕES
# ============================================================

import turtle
import random

# ------------------------------------------------------------
# 1. SCREEN SETUP / CONFIGURAÇÃO DA TELA
# ------------------------------------------------------------

screen = turtle.Screen()
screen.title("BALLOON POPPER - Click the Balloon!")
screen.bgcolor("#172554")
screen.setup(width=800, height=600)
screen.tracer(0)

# ------------------------------------------------------------
# 2. GAME VARIABLES / VARIÁVEIS DO JOGO
# ------------------------------------------------------------

score = 0
time_left = 30
game_running = True

colors = ["red", "orange", "yellow", "pink", "purple", "cyan"]

# ------------------------------------------------------------
# 3. CREATE BALLOON / CRIAR BALÃO
# ------------------------------------------------------------

balloon = turtle.Turtle()
balloon.shape("circle")
balloon.penup()
balloon.speed(0)
balloon.shapesize(2.5)
balloon.color(random.choice(colors))

# ------------------------------------------------------------
# 4. SCOREBOARD / PLACAR
# ------------------------------------------------------------

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")

def update_score():
    score_display.clear()
    score_display.goto(0, 250)

    score_display.write(
        f"SCORE: {score}     TIME: {time_left}s",
        align="center",
        font=("Arial", 20, "bold")
    )

# ------------------------------------------------------------
# 5. MOVE BALLOON / MOVIMENTAR BALÃO
# ------------------------------------------------------------

def move_balloon():
    x = random.randint(-350, 350)
    y = random.randint(-200, 180)

    balloon.goto(x, y)
    balloon.color(random.choice(colors))

# ------------------------------------------------------------
# 6. POP BALLOON / ESTOURAR BALÃO
# ------------------------------------------------------------

def pop_balloon(x, y):
    global score

    if not game_running:
        return

    score += 1

    update_score()
    move_balloon()

    screen.update()

# Detecta o clique esquerdo do mouse.
# Detects the left mouse button click.
balloon.onclick(pop_balloon, btn=1)

# ------------------------------------------------------------
# 7. COUNTDOWN / CONTAGEM REGRESSIVA
# ------------------------------------------------------------

def countdown():
    global time_left, game_running

    if not game_running:
        return

    if time_left > 0:
        time_left -= 1
        update_score()
        screen.update()

        screen.ontimer(countdown, 1000)

    else:
        finish_game()

# ------------------------------------------------------------
# 8. GAME OVER / FIM DO JOGO
# ------------------------------------------------------------

def finish_game():
    global game_running

    game_running = False
    balloon.hideturtle()

    score_display.clear()
    score_display.goto(0, 40)

    score_display.write(
        "GAME OVER!",
        align="center",
        font=("Arial", 32, "bold")
    )

    score_display.goto(0, -10)

    score_display.write(
        f"YOUR SCORE: {score}",
        align="center",
        font=("Arial", 22, "bold")
    )

    score_display.goto(0, -60)

    score_display.write(
        "Close the window to exit",
        align="center",
        font=("Arial", 14, "normal")
    )

    screen.update()

# ------------------------------------------------------------
# 9. START GAME / INICIAR JOGO
# ------------------------------------------------------------

move_balloon()
update_score()

screen.update()

screen.ontimer(countdown, 1000)

# Mantém o jogo ativo e recebe os cliques.
# Keeps the game running and receives mouse clicks.
screen.mainloop()

# ============================================================
# END OF GAME / FIM DO JOGO
# ============================================================
