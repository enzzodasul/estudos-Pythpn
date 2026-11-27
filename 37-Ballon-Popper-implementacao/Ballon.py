
from turtle import *

# Configurações / Settings
diameter = 40
pop_diameter = 100

# Desenhar balão / Draw balloon
def draw_balloon():
    clear()
    color("purple")
    dot(diameter)

# Inflar balão / Inflate balloon
def inflate_balloon():
    global diameter

    diameter += 10

    if diameter >= pop_diameter:
        print("Estourou!")

        clear()
        color("red")
        write("POP!", align="center", font=("Arial", 30, "bold"))

        diameter = 40

    else:
        draw_balloon()

# Desenhar balão inicial / Draw initial balloon
draw_balloon()

# Configurar teclado / Keyboard setup
screen = Screen()
screen.listen()
screen.onkey(inflate_balloon, "Up")

done()

