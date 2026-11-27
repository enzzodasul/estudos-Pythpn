
import turtle
import random

# ==========================================
# BALLOON POPPER - SKY ADVENTURE
# Jogo de estourar balões / Balloon popping game
# ==========================================

# CONFIGURAÇÃO DA TELA / SCREEN SETUP
screen = turtle.Screen()
screen.title("Balloon Popper - Sky Adventure")
screen.bgcolor("#87CEEB")
screen.setup(width=900, height=650)
screen.tracer(0)

# VARIÁVEIS DO JOGO / GAME VARIABLES
score = 0
time_left = 30
game_running = True

colors = [
    "#FF4D6D",
    "#FFD166",
    "#06D6A0",
    "#9B5DE5",
    "#F15BB5",
    "#00BBF9",
    "#FF9F1C",
    "#FFFFFF"
]

# ==========================================
# DESENHAR ELEMENTOS DO CENÁRIO
# DRAW SCENERY ELEMENTS
# ==========================================

# Sol / Sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.goto(350, 250)
sun.dot(90, "#FFD166")

# Nuvens / Clouds
clouds = turtle.Turtle()
clouds.hideturtle()
clouds.penup()

for x, y in [(-350, 220), (-100, 260), (150, 190), (350, 100)]:
    for dx, dy, size in [
        (-25, 0, 45),
        (0, 15, 55),
        (30, 0, 45),
        (5, -10, 45)
    ]:
        clouds.goto(x + dx, y + dy)
        clouds.dot(size, "white")

# ==========================================
# PAINEL DE PONTUAÇÃO
# SCOREBOARD
# ==========================================

panel = turtle.Turtle()
panel.hideturtle()
panel.penup()
panel.color("#17324D")

def update_panel():
    panel.clear()
    panel.goto(0, 275)
    panel.write(
        f"SCORE: {score}       TIME: {time_left}s",
        align="center",
        font=("Arial", 22, "bold")
    )

# ==========================================
# CRIAR OS BALÕES
# CREATE THE BALLOONS
# ==========================================

balloons = []

def create_balloon():
    balloon = turtle.Turtle()
    balloon.shape("circle")
    balloon.penup()
    balloon.speed(0)
    balloon.shapesize(stretch_wid=1.8, stretch_len=1.3)
    balloon.color(random.choice(colors))

    balloon.goto(
        random.randint(-400, 400),
        random.randint(-320, -100)
    )

    # Velocidade de subida / Rising speed
    balloon.rise_speed = random.uniform(1.0, 3.0)

    balloons.append(balloon)

    # Evento de clique / Click event
    balloon.onclick(
        lambda x, y, b=balloon: pop_balloon(b)
    )

# Criar 8 balões / Create 8 balloons
for _ in range(8):
    create_balloon()

# ==========================================
# CORDAS DOS BALÕES
# BALLOON STRINGS
# ==========================================

strings = turtle.Turtle()
strings.hideturtle()
strings.speed(0)
strings.color("#52616B")
strings.penup()

def draw_strings():
    strings.clear()

    for balloon in balloons:
        if balloon.isvisible():
            x = balloon.xcor()
            y = balloon.ycor()

            strings.penup()
            strings.goto(x, y - 25)
            strings.pendown()
            strings.goto(x + 3, y - 55)
            strings.penup()

# ==========================================
# ESTOURAR BALÃO
# POP BALLOON
# ==========================================

def pop_balloon(balloon):
    global score

    if not game_running:
        return

    score += 1

    # Efeito de estouro / Pop effect
    balloon.hideturtle()

    # Reposicionar balão / Reposition balloon
    balloon.goto(
        random.randint(-400, 400),
        random.randint(-320, -100)
    )

    balloon.color(random.choice(colors))
    balloon.rise_speed = random.uniform(1.0, 3.0)
    balloon.showturtle()

    update_panel()
    screen.update()

# ==========================================
# MOVIMENTAR OS BALÕES
# MOVE THE BALLOONS
# ==========================================

def move_balloons():
    if not game_running:
        return

    for balloon in balloons:
        new_y = balloon.ycor() + balloon.rise_speed

        # Quando chegar ao topo, volta para baixo
        # When it reaches the top, return to the bottom
        if new_y > 330:
            balloon.goto(
                random.randint(-400, 400),
                random.randint(-350, -150)
            )
            balloon.color(random.choice(colors))
            balloon.rise_speed = random.uniform(1.0, 3.0)
        else:
            balloon.sety(new_y)

    draw_strings()

    screen.update()
    screen.ontimer(move_balloons, 30)

# ==========================================
# CRONÔMETRO
# COUNTDOWN TIMER
# ==========================================

def countdown():
    global time_left

    if not game_running:
        return

    if time_left > 0:
        time_left -= 1
        update_panel()
        screen.update()
        screen.ontimer(countdown, 1000)
    else:
        finish_game()

# ==========================================
# FIM DO JOGO
# GAME OVER
# ==========================================

def finish_game():
    global game_running

    game_running = False

    for balloon in balloons:
        balloon.hideturtle()

    strings.clear()
    panel.clear()

    panel.goto(0, 60)
    panel.color("#17324D")
    panel.write(
        "GAME OVER!",
        align="center",
        font=("Arial", 40, "bold")
    )

    panel.goto(0, 0)
    panel.write(
        f"YOUR SCORE: {score}",
        align="center",
        font=("Arial", 28, "bold")
    )

    panel.goto(0, -50)
    panel.write(
        "Thanks for playing!",
        align="center",
        font=("Arial", 18, "normal")
    )

    screen.update()

# ==========================================
# INICIAR O JOGO
# START THE GAME
# ==========================================

update_panel()
draw_strings()

move_balloons()
screen.ontimer(countdown, 1000)

screen.mainloop()
