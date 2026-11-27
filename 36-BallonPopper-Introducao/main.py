
# ============================================================
# BALLOON POPPER - INTRODUÇÃO
# BALLOON POPPER - INTRODUCTION
# ============================================================

# 1. O QUE É BALLOON POPPER? / WHAT IS BALLOON POPPER?
#
# Balloon Popper é um jogo simples em que o jogador precisa
# estourar balões que aparecem na tela.
#
# Balloon Popper is a simple game where the player needs
# to pop balloons that appear on the screen.
#
# Conceitos utilizados / Concepts used:
# - Turtle: criação gráfica / Graphics
# - Functions: funções / Functions
# - Loops: repetições / Loops
# - Events: eventos do teclado e mouse / Keyboard and mouse events
# - Coordinates: coordenadas / Coordinates
# - Collision detection: detecção de colisões


# ------------------------------------------------------------
# 2. IMPORTANDO AS BIBLIOTECAS / IMPORTING LIBRARIES
# ------------------------------------------------------------

import turtle
import random

# turtle: cria a interface gráfica / Creates the graphical interface
# random: gera posições aleatórias / Generates random positions


# ------------------------------------------------------------
# 3. CONFIGURANDO A TELA / SETTING UP THE SCREEN
# ------------------------------------------------------------

tela = turtle.Screen()

tela.title("Balloon Popper")
tela.bgcolor("lightblue")
tela.setup(width=800, height=600)


# ------------------------------------------------------------
# 4. CRIANDO UM BALÃO / CREATING A BALLOON
# ------------------------------------------------------------

balao = turtle.Turtle()

balao.shape("circle")
balao.color("red")
balao.penup()

balao.goto(0, 0)

# goto(x, y): posiciona a tartaruga nas coordenadas indicadas.
# goto(x, y): moves the turtle to the specified coordinates.


# ------------------------------------------------------------
# 5. MOVIMENTAÇÃO ALEATÓRIA / RANDOM MOVEMENT
# ------------------------------------------------------------

def mover_balao():
    # Gera coordenadas aleatórias / Generates random coordinates
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)

    balao.goto(x, y)


# Executa a função / Calls the function
mover_balao()


# ------------------------------------------------------------
# 6. ESTOURANDO O BALÃO / POPPING THE BALLOON
# ------------------------------------------------------------

def estourar_balao(x, y):
    # Esconde o balão / Hides the balloon
    balao.hideturtle()

    print("Balão estourado! / Balloon popped!")

    # Move para outra posição / Moves to another position
    mover_balao()

    # Mostra novamente / Shows again
    balao.showturtle()


# onclick(): executa uma função quando o objeto é clicado.
# onclick(): executes a function when the object is clicked.

balao.onclick(estourar_balao)


# ------------------------------------------------------------
# 7. CONTADOR DE PONTOS / SCORE COUNTER
# ------------------------------------------------------------

pontos = 0

placar = turtle.Turtle()
placar.hideturtle()
placar.penup()
placar.goto(-350, 250)

def atualizar_placar():
    placar.clear()
    placar.write(
        f"Pontos: {pontos}",
        font=("Arial", 18, "bold")
    )


# ------------------------------------------------------------
# 8. FUNÇÃO PARA CONTAR OS ACERTOS
# FUNCTION TO COUNT SUCCESSFUL CLICKS
# ------------------------------------------------------------

def estourar_balao(x, y):
    global pontos

    pontos += 1

    print("Balão estourado! / Balloon popped!")

    atualizar_placar()
    mover_balao()


# Vincula o clique à função / Connects the click to the function
balao.onclick(estourar_balao)

atualizar_placar()


# ------------------------------------------------------------
# 9. CÓDIGO COMPLETO / COMPLETE CODE
# ------------------------------------------------------------

import turtle
import random

# Configuração da tela / Screen setup
tela = turtle.Screen()
tela.title("Balloon Popper")
tela.bgcolor("lightblue")
tela.setup(width=800, height=600)

# Criação do balão / Balloon creation
balao = turtle.Turtle()
balao.shape("circle")
balao.color("red")
balao.penup()
balao.shapesize(2)

# Criação do placar / Scoreboard creation
placar = turtle.Turtle()
placar.hideturtle()
placar.penup()
placar.goto(-350, 250)

pontos = 0

# Movimenta o balão / Moves the balloon
def mover_balao():
    x = random.randint(-350, 350)
    y = random.randint(-250, 220)
    balao.goto(x, y)


# Atualiza a pontuação / Updates the score
def atualizar_placar():
    placar.clear()
    placar.write(
        f"Pontos: {pontos}",
        font=("Arial", 18, "bold")
    )


# Evento de clique / Click event
def estourar_balao(x, y):
    global pontos

    pontos += 1

    atualizar_placar()
    mover_balao()


# Configuração inicial / Initial setup
balao.onclick(estourar_balao)

mover_balao()
atualizar_placar()

# Mantém o jogo aberto / Keeps the game running
turtle.done()


# ============================================================
# 10. PRINCIPAIS COMANDOS / MAIN COMMANDS
# ============================================================

# turtle.Screen()  -> Cria a tela / Creates the screen
# turtle.Turtle()  -> Cria um objeto gráfico / Creates a turtle
# shape("circle")  -> Define o formato / Sets the shape
# color("red")     -> Define a cor / Sets the color
# penup()          -> Levanta a caneta / Lifts the pen
# goto(x, y)       -> Move para uma posição / Moves to a position
# onclick(funcao)  -> Detecta cliques / Detects clicks
# hideturtle()     -> Esconde o objeto / Hides the object
# showturtle()     -> Mostra o objeto / Shows the object
# random.randint() -> Gera números aleatórios / Generates random numbers
# clear()          -> Limpa o texto / Clears the text
# write()          -> Escreve na tela / Writes on the screen
# turtle.done()    -> Mantém a janela aberta / Keeps the window open


# ============================================================
# 11. RESUMO / SUMMARY
# ============================================================

# Balloon Popper:
# Jogo de clicar em balões para ganhar pontos.
# A game where you click balloons to earn points.

# random:
# Gera posições aleatórias para os balões.
# Generates random positions for balloons.

# onclick():
# Detecta quando o jogador clica no balão.
# Detects when the player clicks the balloon.

# global:
# Permite modificar uma variável global dentro de uma função.
# Allows modifying a global variable inside a function.

# Funções:
# Organizam as ações do jogo em blocos reutilizáveis.
# Organize game actions into reusable blocks.

# Pontuação / Score:
# Armazena e exibe a quantidade de balões estourados.
# Stores and displays the number of popped balloons.
