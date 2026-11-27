
import turtle
import random
import math
import time

# ============================================================
# BALLOON POPPER - DELUXE EDITION
# A complete animated arcade game made with Python Turtle
# ============================================================

# ---------------- CONFIGURATION -----------------------------

WIDTH = 1100
HEIGHT = 750
FPS_DELAY = 25
GAME_DURATION = 60
BALLOON_COUNT = 12

COLORS = [
    "#FF477E",
    "#FF9F1C",
    "#FFD93D",
    "#20C997",
    "#36A9FF",
    "#A78BFA",
    "#F472B6",
    "#F8FAFC",
]

# ---------------- SCREEN ------------------------------------

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("BALLOON POPPER - DELUXE EDITION")
screen.bgcolor("#172B55")
screen.tracer(0)

# ---------------- GAME STATE --------------------------------

score = 0
time_left = GAME_DURATION
combo = 0
best_combo = 0
last_click = 0

game_running = False
game_started = False

balloons = []
particles = []

# ---------------- TURTLE HELPERS ---------------------------

def create_pen():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()
    return pen


background = create_pen()
interface = create_pen()


def draw_rectangle(pen, x, y, width, height, color):
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


def draw_dot(pen, x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.dot(size, color)


# ============================================================
# BACKGROUND - CENÁRIO
# ============================================================

def draw_background():

    # Sunset gradient / Degradê do pôr do sol
    sky_bands = [
        (-375, "#172B55"),
        (-285, "#233D70"),
        (-195, "#345B88"),
        (-105, "#4C7FA5"),
        (-15, "#79A8BD"),
        (75, "#B9A0B1"),
        (165, "#E9A47E"),
        (255, "#FFD18B"),
    ]

    for y, color in sky_bands:
        draw_rectangle(
            background,
            -550,
            y,
            1100,
            100,
            color
        )

    # Sun / Sol
    draw_dot(background, 370, 215, 150, "#F5B477")
    draw_dot(background, 370, 215, 115, "#FFD77B")
    draw_dot(background, 370, 215, 85, "#FFF0B3")

    # Stars / Estrelas
    for _ in range(75):
        x = random.randint(-530, 530)
        y = random.randint(100, 355)

        draw_dot(
            background,
            x,
            y,
            random.randint(2, 5),
            "#FFF4D6"
        )

    # Distant mountains / Montanhas distantes
    for x in range(-600, 600, 110):
        peak_y = random.randint(-210, -125)

        background.goto(x, -340)
        background.color("#263D60")
        background.begin_fill()
        background.pendown()

        background.goto(x + 65, peak_y)
        background.goto(x + 150, -340)
        background.goto(x, -340)

        background.end_fill()
        background.penup()

    # Front hills / Colinas
    for x in range(-600, 600, 180):
        background.goto(x, -340)
        background.color("#1C354B")
        background.begin_fill()
        background.pendown()

        background.goto(x + 90, -260)
        background.goto(x + 180, -340)
        background.goto(x, -340)

        background.end_fill()
        background.penup()

    # Clouds / Nuvens
    cloud_positions = [
        (-420, 190),
        (-180, 245),
        (70, 175),
        (460, 90),
        (-470, 5),
    ]

    for x, y in cloud_positions:
        for dx, dy, size in [
            (-30, 0, 48),
            (0, 15, 65),
            (35, 0, 52),
            (5, -12, 48),
        ]:
            draw_dot(
                background,
                x + dx,
                y + dy,
                size,
                "#F5F6F7"
            )

    # Ground / Chão
    draw_rectangle(
        background,
        -550,
        -375,
        1100,
        35,
        "#142A3B"
    )


draw_background()


# ============================================================
# BALLOON CLASS
# ============================================================

class Balloon:

    def __init__(self, x, y):

        # Balloon body / Corpo
        self.body = turtle.Turtle()
        self.body.shape("circle")
        self.body.penup()
        self.body.speed(0)
        self.body.shapesize(
            stretch_wid=1.65,
            stretch_len=1.25
        )

        # Balloon highlight / Brilho
        self.highlight = turtle.Turtle()
        self.highlight.shape("circle")
        self.highlight.penup()
        self.highlight.speed(0)
        self.highlight.color("#FFFFFF")
        self.highlight.shapesize(
            stretch_wid=0.18,
            stretch_len=0.15
        )

        # Balloon knot / Nó
        self.knot = turtle.Turtle()
        self.knot.shape("triangle")
        self.knot.penup()
        self.knot.speed(0)
        self.knot.setheading(180)
        self.knot.shapesize(0.3, 0.3)

        # Balloon string / Corda
        self.string = turtle.Turtle()
        self.string.shape("square")
        self.string.penup()
        self.string.speed(0)
        self.string.color("#E8D6B0")
        self.string.shapesize(
            stretch_wid=0.035,
            stretch_len=0.75
        )
        self.string.setheading(270)

        # Basket / Cesto
        self.basket = turtle.Turtle()
        self.basket.shape("square")
        self.basket.penup()
        self.basket.speed(0)
        self.basket.color("#A66B3F")
        self.basket.shapesize(0.28, 0.4)

        self.x = x
        self.y = y

        self.speed = random.uniform(0.8, 2.1)
        self.phase = random.uniform(0, math.pi * 2)

        self.points = random.choice([10, 10, 20, 20, 30])

        self.set_color(random.choice(COLORS))
        self.update_position()

        self.body.onclick(
            lambda x, y, balloon=self: pop_balloon(balloon)
        )

    def set_color(self, color):

        self.color = color
        self.body.color(color)

        self.highlight.color("#FFFFFF")
        self.knot.color(color)

    def update_position(self):

        self.body.goto(self.x, self.y)

        self.highlight.goto(
            self.x - 8,
            self.y + 14
        )

        self.knot.goto(
            self.x,
            self.y - 31
        )

        self.string.goto(
            self.x + 1,
            self.y - 44
        )

        self.basket.goto(
            self.x + 2,
            self.y - 61
        )

    def move(self):

        self.phase += 0.045

        # Gentle floating motion / Movimento flutuante
        self.x += math.sin(self.phase) * 0.65
        self.y += self.speed

        if self.y > 395:
            self.reset()

        self.update_position()

    def reset(self):

        self.x = random.randint(-500, 500)
        self.y = random.randint(-390, -150)

        self.speed = random.uniform(0.8, 2.5)
        self.phase = random.uniform(0, math.pi * 2)

        self.points = random.choice([10, 10, 20, 20, 30])

        self.set_color(random.choice(COLORS))

    def hide(self):

        self.body.hideturtle()
        self.highlight.hideturtle()
        self.knot.hideturtle()
        self.string.hideturtle()
        self.basket.hideturtle()

    def show(self):

        self.body.showturtle()
        self.highlight.showturtle()
        self.knot.showturtle()
        self.string.showturtle()
        self.basket.showturtle()


# ============================================================
# PARTICLE SYSTEM - EXPLOSIONS
# ============================================================

class Particle:

    def __init__(self, x, y, color):

        self.sprite = turtle.Turtle()
        self.sprite.shape("circle")
        self.sprite.penup()
        self.sprite.speed(0)

        self.sprite.color(color)

        size = random.uniform(0.12, 0.35)
        self.sprite.shapesize(size, size)

        self.sprite.goto(x, y)

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 7)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(12, 22)

    def update(self):

        x = self.sprite.xcor() + self.vx
        y = self.sprite.ycor() + self.vy

        self.vy -= 0.18

        self.sprite.goto(x, y)

        self.life -= 1

        if self.life <= 0:
            self.sprite.hideturtle()
            return False

        return True


def create_explosion(x, y, color):

    for _ in range(16):
        particles.append(
            Particle(x, y, color)
        )


# ============================================================
# USER INTERFACE
# ============================================================

def draw_interface():

    interface.clear()

    # Main title
    interface.goto(0, 322)
    interface.color("#FFFFFF")

    interface.write(
        "BALLOON POPPER",
        align="center",
        font=("Arial", 27, "bold")
    )

    # Subtitle
    interface.goto(0, 287)
    interface.color("#FFE8A3")

    interface.write(
        "DELUXE SKY FESTIVAL",
        align="center",
        font=("Arial", 12, "bold")
    )

    # Score
    interface.goto(-490, 320)
    interface.color("#FFFFFF")

    interface.write(
        f"SCORE: {score}",
        font=("Arial", 17, "bold")
    )

    # Timer
    interface.goto(365, 320)

    interface.write(
        f"TIME: {time_left}s",
        font=("Arial", 17, "bold")
    )

    # Combo
    interface.goto(0, 245)
    interface.color("#FFD166")

    interface.write(
        f"COMBO x{combo}",
        align="center",
        font=("Arial", 17, "bold")
    )


# ============================================================
# POP BALLOON
# ============================================================

def pop_balloon(balloon):

    global score
    global combo
    global best_combo
    global last_click

    if not game_running:
        return

    current_time = time.monotonic()

    # Combo system
    if current_time - last_click < 1.5:
        combo += 1
    else:
        combo = 1

    last_click = current_time

    best_combo = max(best_combo, combo)

    multiplier = min(combo, 5)

    points = balloon.points * multiplier

    score += points

    # Explosion at balloon position
    x = balloon.x
    y = balloon.y
    color = balloon.color

    create_explosion(x, y, color)

    # Respawn balloon
    balloon.reset()
    balloon.update_position()

    draw_interface()
    screen.update()


# ============================================================
# CREATE BALLOONS
# ============================================================

def create_balloons():

    for _ in range(BALLOON_COUNT):

        balloon = Balloon(
            random.randint(-500, 500),
            random.randint(-350, 250)
        )

        balloons.append(balloon)


# ============================================================
# ANIMATION LOOP
# ============================================================

def animate():

    if not game_running:
        return

    # Move balloons
    for balloon in balloons:
        balloon.move()

    # Update particles
    for particle in particles[:]:

        if not particle.update():
            particles.remove(particle)

    screen.update()

    screen.ontimer(
        animate,
        FPS_DELAY
    )


# ============================================================
# COUNTDOWN
# ============================================================

def countdown():

    global time_left

    if not game_running:
        return

    if time_left > 0:

        time_left -= 1

        draw_interface()
        screen.update()

        screen.ontimer(
            countdown,
            1000
        )

    else:
        finish_game()


# ============================================================
# START SCREEN
# ============================================================

def draw_start_screen():

    interface.goto(0, 105)
    interface.color("#FFFFFF")

    interface.write(
        "WELCOME TO THE SKY FESTIVAL",
        align="center",
        font=("Arial", 27, "bold")
    )

    interface.goto(0, 45)
    interface.color("#FFE8A3")

    interface.write(
        "POP BALLOONS AND BUILD YOUR COMBO!",
        align="center",
        font=("Arial", 16, "bold")
    )

    interface.goto(0, -25)
    interface.color("#FFFFFF")

    interface.write(
        "CLICK ANYWHERE TO START",
        align="center",
        font=("Arial", 19, "bold")
    )

    interface.goto(0, -80)

    interface.write(
        "60 SECONDS  |  10, 20 OR 30 POINTS",
        align="center",
        font=("Arial", 12, "normal")
    )

    interface.goto(0, -125)
    interface.color("#DCEBFA")

    interface.write(
        "Click the balloons as fast as you can!",
        align="center",
        font=("Arial", 13, "normal")
    )

    screen.update()


# ============================================================
# START GAME
# ============================================================

def start_game(x=None, y=None):

    global game_running
    global game_started

    if game_started:
        return

    game_started = True
    game_running = True

    # Remove start screen
    interface.clear()

    # Disable the start click event
    screen.onclick(None)

    create_balloons()

    draw_interface()

    # Start animation and timer
    animate()

    screen.ontimer(
        countdown,
        1000
    )

    screen.update()


# ============================================================
# GAME OVER
# ============================================================

def finish_game():

    global game_running

    game_running = False

    # Hide all balloons
    for balloon in balloons:
        balloon.hide()

    # Remove remaining particles
    for particle in particles:
        particle.sprite.hideturtle()

    particles.clear()

    interface.clear()

    interface.goto(0, 105)
    interface.color("#FFE8A3")

    interface.write(
        "GAME OVER!",
        align="center",
        font=("Arial", 45, "bold")
    )

    interface.goto(0, 35)
    interface.color("#FFFFFF")

    interface.write(
        f"FINAL SCORE: {score}",
        align="center",
        font=("Arial", 28, "bold")
    )

    interface.goto(0, -25)
    interface.color("#FFD166")

    interface.write(
        f"BEST COMBO: x{best_combo}",
        align="center",
        font=("Arial", 21, "bold")
    )

    interface.goto(0, -95)
    interface.color("#FFFFFF")

    interface.write(
        "THANK YOU FOR PLAYING!",
        align="center",
        font=("Arial", 17, "normal")
    )

    interface.goto(0, -145)

    interface.write(
        "Close the window to exit",
        align="center",
        font=("Arial", 12, "normal")
    )

    screen.update()


# ============================================================
# INITIALIZE GAME
# ============================================================

draw_start_screen()

screen.onclick(start_game)

screen.mainloop()
