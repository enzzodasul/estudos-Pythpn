
# ============================================================
# PYTHON TURTLE - INTRODUÇÃO
# PYTHON TURTLE - INTRODUCTION
# ============================================================

# 1. O QUE É TURTLE? / WHAT IS TURTLE?
#
# Turtle é uma biblioteca do Python utilizada para criar desenhos,
# formas geométricas e animações através de comandos.
#
# Turtle is a Python library used to create drawings,
# geometric shapes, and animations through commands.
#
# A tartaruga funciona como uma caneta que se movimenta pela tela.
# The turtle works like a pen that moves around the screen.
#
# Importação / Import:
# import turtle


# ------------------------------------------------------------
# 2. IMPORTANDO A BIBLIOTECA / IMPORTING THE LIBRARY
# ------------------------------------------------------------

import turtle

# Cria a tartaruga / Creates the turtle
t = turtle.Turtle()

# Mantém a janela aberta / Keeps the window open
turtle.done()


# ------------------------------------------------------------
# 3. MOVIMENTAÇÃO BÁSICA / BASIC MOVEMENT
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.forward(100)   # Move 100 pixels para frente / Move forward
t.backward(50)   # Move 50 pixels para trás / Move backward
t.right(90)      # Gira 90 graus à direita / Turn right
t.left(90)       # Gira 90 graus à esquerda / Turn left

turtle.done()


# ------------------------------------------------------------
# 4. DESENHANDO FORMAS GEOMÉTRICAS / DRAWING SHAPES
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

# Quadrado / Square
for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()


# Triângulo / Triangle
import turtle

t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()


# Retângulo / Rectangle
import turtle

t = turtle.Turtle()

for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(80)
    t.right(90)

turtle.done()


# ------------------------------------------------------------
# 5. CONTROLE DA CANETA / PEN CONTROL
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.penup()       # Levanta a caneta / Lifts the pen
t.forward(100)  # Move sem desenhar / Moves without drawing

t.pendown()     # Abaixa a caneta / Puts the pen down
t.forward(100)  # Move desenhando / Moves while drawing

turtle.done()


# ------------------------------------------------------------
# 6. CORES / COLORS
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.color("red")          # Cor da linha / Pen color
t.forward(100)

turtle.done()


# Outras cores / Other colors:
# "blue"       = Azul
# "green"      = Verde
# "yellow"     = Amarelo
# "orange"     = Laranja
# "purple"     = Roxo
# "black"      = Preto
# "white"      = Branco
# "pink"       = Rosa


# ------------------------------------------------------------
# 7. ESPESSURA DA LINHA / LINE WIDTH
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.pensize(5)  # Define a espessura / Sets the line width
t.forward(150)

turtle.done()


# ------------------------------------------------------------
# 8. COR DE PREENCHIMENTO / FILL COLOR
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.fillcolor("blue")  # Define a cor de preenchimento / Fill color

t.begin_fill()       # Inicia o preenchimento / Starts filling

for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()         # Finaliza o preenchimento / Ends filling

turtle.done()


# ------------------------------------------------------------
# 9. VELOCIDADE DA TARTARUGA / TURTLE SPEED
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.speed(1)  # Lenta / Slow
t.forward(100)

# Valores de velocidade / Speed values:
# 1 = Lenta / Slow
# 5 = Média / Medium
# 10 = Rápida / Fast
# 0 = Máxima velocidade / Fastest

turtle.done()


# ------------------------------------------------------------
# 10. FORMATO DA TARTARUGA / TURTLE SHAPE
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.shape("turtle")  # Formato de tartaruga / Turtle shape

# Outros formatos / Other shapes:
# "arrow"    = Seta
# "circle"   = Círculo
# "square"   = Quadrado
# "triangle" = Triângulo
# "classic"  = Clássico

turtle.done()


# ------------------------------------------------------------
# 11. COR DE FUNDO / BACKGROUND COLOR
# ------------------------------------------------------------

import turtle

tela = turtle.Screen()

tela.bgcolor("lightblue")  # Define o fundo / Sets background color

t = turtle.Turtle()
t.forward(100)

turtle.done()


# ------------------------------------------------------------
# 12. ESCREVER NA TELA / WRITE ON SCREEN
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.write("Olá, Python!", font=("Arial", 20, "bold"))

turtle.done()


# ------------------------------------------------------------
# 13. LIMPAR E REINICIAR / CLEAR AND RESET
# ------------------------------------------------------------

import turtle

t = turtle.Turtle()

t.forward(100)
t.right(90)

t.clear()  # Apaga os desenhos feitos pela tartaruga / Clears drawings

# reset() também apaga e restaura as configurações iniciais.
# reset() also clears and restores the initial settings.

turtle.done()


# ------------------------------------------------------------
# 14. PRINCIPAIS COMANDOS / MAIN COMMANDS
# ------------------------------------------------------------

# turtle.Turtle()  -> Cria uma tartaruga / Creates a turtle
# forward(100)     -> Move para frente / Move forward
# backward(100)    -> Move para trás / Move backward
# right(90)        -> Gira à direita / Turn right
# left(90)         -> Gira à esquerda / Turn left
# penup()          -> Levanta a caneta / Lift the pen
# pendown()        -> Abaixa a caneta / Lower the pen
# color("red")     -> Define a cor / Sets the color
# pensize(5)       -> Define a espessura / Sets line width
# speed(5)         -> Define a velocidade / Sets the speed
# shape("turtle")  -> Define o formato / Sets the shape
# fillcolor("red") -> Define o preenchimento / Sets fill color
# begin_fill()     -> Inicia preenchimento / Starts filling
# end_fill()       -> Finaliza preenchimento / Ends filling
# clear()          -> Limpa os desenhos / Clears drawings
# reset()          -> Reinicia a tartaruga / Resets the turtle
# write("Texto")   -> Escreve na tela / Writes on screen
# turtle.done()    -> Mantém a janela aberta / Keeps window open


# ------------------------------------------------------------
# 15. EXEMPLO PRÁTICO / PRACTICAL EXAMPLE
# ------------------------------------------------------------

import turtle

# Configuração da tela / Screen configuration
tela = turtle.Screen()
tela.title("Meu primeiro desenho com Turtle")
tela.bgcolor("lightblue")

# Criação da tartaruga / Creating the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen")
t.pensize(4)
t.speed(5)

# Desenhando um quadrado / Drawing a square
t.begin_fill()
t.fillcolor("yellow")

for i in range(4):
    t.forward(120)
    t.right(90)

t.end_fill()

# Escrevendo na tela / Writing on screen
t.penup()
t.goto(-60, -40)
t.color("black")
t.write("Meu quadrado!", font=("Arial", 14, "bold"))

turtle.done()


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# Turtle é uma biblioteca gráfica do Python.
# Turtle is a graphics library in Python.

# Permite desenhar utilizando comandos de movimentação.
# It allows drawing using movement commands.

# forward() e backward() movimentam a tartaruga.
# forward() and backward() move the turtle.

# right() e left() controlam a direção.
# right() and left() control the direction.

# penup() e pendown() controlam o desenho.
# penup() and pendown() control drawing.

# color() altera a cor da linha.
# color() changes the pen color.

# begin_fill() e end_fill() preenchem formas.
# begin_fill() and end_fill() fill shapes.

# turtle.done() mantém a janela aberta.
# turtle.done() keeps the window open.
