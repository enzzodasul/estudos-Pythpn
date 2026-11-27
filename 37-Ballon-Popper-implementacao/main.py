
# ================================================================
# PYTHON TURTLE - BALLOON POPPER
# GUIA DE ESTUDO: COMANDOS, SINTAXES E EXPLICAÇÕES
# STUDY GUIDE: COMMANDS, SYNTAXES AND EXPLANATIONS
# ================================================================
#
# OBJETIVO / PURPOSE:
# Aprender os principais comandos da biblioteca Turtle
# através de um pequeno jogo de inflar e estourar um balão.
#
# Learn the main Turtle library commands through a small
# balloon inflation and popping game.
#
# COMO EXECUTAR / HOW TO RUN:
# python exemple.py
#
# CONTROLES / CONTROLS:
# Seta para cima (UP): inflar o balão / Inflate the balloon.
#
# ================================================================
# 1. IMPORTAÇÃO DE BIBLIOTECAS / IMPORTING LIBRARIES
# ================================================================

# from turtle import *
#
# IMPORT:
# Importa comandos e funcionalidades de uma biblioteca.
# Imports commands and features from a library.
#
# FROM:
# Indica de qual biblioteca queremos importar.
# Indicates which library we want to import from.
#
# TURTLE:
# Biblioteca gráfica do Python para desenhar e criar animações.
# Python graphics library for drawing and creating animations.
#
# IMPORT *:
# Importa todos os nomes públicos da biblioteca.
# Imports all public names from the library.
#
# ATENÇÃO / WARNING:
# O asterisco (*) permite usar diretamente color(), dot(),
# clear(), Screen() e outros comandos, sem escrever turtle.
#
# The asterisk (*) lets us use commands directly without
# writing turtle.color(), turtle.dot(), etc.

from turtle import *


# ================================================================
# 2. VARIÁVEIS / VARIABLES
# ================================================================

# Variáveis armazenam informações que podem ser utilizadas
# e modificadas durante a execução do programa.
#
# Variables store information that can be used and changed
# while the program is running.

diameter = 40

# diameter:
# Guarda o tamanho atual do balão.
# Stores the current balloon size.

pop_diameter = 100

# pop_diameter:
# Define o tamanho necessário para estourar o balão.
# Defines the size required to pop the balloon.

# TIPOS DE DADOS / DATA TYPES:
#
# 40    -> int (número inteiro / integer)
# 40.5  -> float (número decimal / floating-point)
# "Oi"  -> str (texto / string)
# True  -> bool (verdadeiro / boolean)
# False -> bool (falso / boolean)


# ================================================================
# 3. FUNÇÕES / FUNCTIONS
# ================================================================

# SINTAXE / SYNTAX:
#
# def nome_da_funcao():
#     comandos
#
# DEF:
# Palavra reservada usada para criar uma função.
# Keyword used to define a function.
#
# NOME_DA_FUNCAO:
# Nome escolhido para identificar a função.
# Name chosen to identify the function.
#
# ():
# Parênteses podem receber parâmetros.
# Parentheses can receive parameters.
#
# :
# Dois-pontos indicam o início do bloco da função.
# A colon indicates the beginning of the function block.
#
# INDENTAÇÃO / INDENTATION:
# Os comandos dentro da função precisam estar indentados.
# Commands inside the function must be indented.
#
# Uma função só executa quando é chamada.
# A function only runs when it is called.


# ------------------------------------------------
# FUNÇÃO 1: DESENHAR O BALÃO
# FUNCTION 1: DRAW THE BALLOON
# ------------------------------------------------

def draw_balloon():

    # CLEAR():
    # Apaga os desenhos feitos pela Turtle.
    # Erases drawings made by Turtle.

    clear()

    # COLOR("purple"):
    # Define a cor utilizada nos desenhos.
    # Sets the drawing color.

    color("purple")

    # DOT(TAMANHO):
    # Desenha um círculo preenchido.
    # Draws a filled circle.
    #
    # diameter é a variável que determina o tamanho.
    # diameter is the variable that determines the size.

    dot(diameter)


# ------------------------------------------------
# FUNÇÃO 2: INFLAR O BALÃO
# FUNCTION 2: INFLATE THE BALLOON
# ------------------------------------------------

def inflate_balloon():

    # GLOBAL:
    # Permite modificar uma variável que foi criada
    # fora da função.
    #
    # Allows us to modify a variable created outside
    # the function.

    global diameter

    # OPERADOR +=:
    # Soma um valor à variável e atualiza seu conteúdo.
    # Adds a value to the variable and updates it.
    #
    # É equivalente a:
    # It is equivalent to:
    #
    # diameter = diameter + 10

    diameter += 10

    # ------------------------------------------------
    # 4. CONDIÇÕES / CONDITIONAL STATEMENTS
    # ------------------------------------------------

    # IF:
    # Executa um bloco de código se a condição for verdadeira.
    # Executes a block of code if the condition is true.
    #
    # >=:
    # Operador de comparação: maior ou igual.
    # Comparison operator: greater than or equal to.
    #
    # SINTAXE / SYNTAX:
    #
    # if condição:
    #     comandos

    if diameter >= pop_diameter:

        # PRINT():
        # Exibe uma mensagem no terminal.
        # Displays a message in the terminal.

        print("Estourou! / It popped!")

        # CLEAR():
        # Limpa o desenho atual.
        # Clears the current drawing.

        clear()

        # COLOR():
        # Muda a cor do próximo desenho ou texto.
        # Changes the color of the next drawing or text.

        color("red")

        # WRITE():
        # Escreve um texto na tela da Turtle.
        # Writes text on the Turtle screen.
        #
        # "POP!" -> texto que será exibido.
        # "POP!" -> text to be displayed.
        #
        # ALIGN:
        # Define o alinhamento do texto.
        # Defines text alignment.
        #
        # "center" -> centralizado / centered.
        #
        # FONT:
        # Define fonte, tamanho e estilo.
        # Defines font, size and style.
        #
        # ("Arial", 30, "bold"):
        # Arial = nome da fonte / font name.
        # 30 = tamanho / size.
        # bold = negrito / bold.

        write(
            "POP!",
            align="center",
            font=("Arial", 30, "bold")
        )

        # Reinicia o tamanho do balão.
        # Resets the balloon size.

        diameter = 40

    # ELSE:
    # Executa quando a condição do IF é falsa.
    # Executes when the IF condition is false.
    #
    # IF / ELSE:
    # Se a condição for verdadeira, executa o IF.
    # Se for falsa, executa o ELSE.
    #
    # If the condition is true, execute IF.
    # Otherwise, execute ELSE.

    else:

        # Desenha novamente o balão com o novo tamanho.
        # Draws the balloon again with its new size.

        draw_balloon()


# ================================================================
# 5. CHAMADA DE FUNÇÃO / FUNCTION CALL
# ================================================================

# CHAMAR UMA FUNÇÃO:
# Escrevemos o nome seguido de parênteses.
# We write the function name followed by parentheses.
#
# draw_balloon()
#
# Isso executa o código que está dentro da função.
# This executes the code inside the function.

# Desenha o balão pela primeira vez.
# Draws the balloon for the first time.

draw_balloon()


# ================================================================
# 6. EVENTOS DE TECLADO / KEYBOARD EVENTS
# ================================================================

# SCREEN():
# Cria ou acessa a janela principal do Turtle.
# Creates or accesses the main Turtle window.

screen = Screen()

# LISTEN():
# Faz a janela receber eventos do teclado.
# Makes the window receive keyboard events.
#
# Sem listen(), os comandos de teclado podem não funcionar.
# Without listen(), keyboard commands may not work.

screen.listen()

# ONKEY():
# Associa uma tecla a uma função.
# Associates a keyboard key with a function.
#
# SINTAXE / SYNTAX:
#
# screen.onkey(funcao, "tecla")
#
# inflate_balloon:
# Nome da função que será executada.
# Name of the function that will be executed.
#
# "Up":
# Tecla de seta para cima.
# Up arrow key.
#
# IMPORTANTE / IMPORTANT:
# Usamos inflate_balloon SEM parênteses.
# We use inflate_balloon WITHOUT parentheses.
#
# Correto / Correct:
# screen.onkey(inflate_balloon, "Up")
#
# Incorreto / Incorrect:
# screen.onkey(inflate_balloon(), "Up")
#
# Sem parênteses, passamos a referência da função.
# Without parentheses, we pass the function reference.
#
# Com parênteses, executaríamos a função imediatamente.
# With parentheses, we would execute the function immediately.

screen.onkey(inflate_balloon, "Up")


# ================================================================
# 7. MANTER A JANELA ABERTA / KEEP THE WINDOW OPEN
# ================================================================

# DONE():
# Mantém a janela do Turtle aberta e aguardando eventos.
# Keeps the Turtle window open and waiting for events.
#
# Sem esse comando, o programa pode terminar e fechar a janela.
# Without this command, the program may finish and close the window.

done()


# ================================================================
# 8. RESUMO DOS PRINCIPAIS COMANDOS / COMMANDS SUMMARY
# ================================================================
#
# IMPORTAÇÃO / IMPORTS:
#
# from turtle import *
# Importa os comandos da biblioteca Turtle.
# Imports Turtle library commands.
#
# VARIÁVEIS / VARIABLES:
#
# diameter = 40
# Cria uma variável com valor 40.
# Creates a variable with value 40.
#
# FUNÇÕES / FUNCTIONS:
#
# def minha_funcao():
# Cria uma função.
# Defines a function.
#
# minha_funcao()
# Executa uma função.
# Calls a function.
#
# VARIÁVEIS GLOBAIS / GLOBAL VARIABLES:
#
# global diameter
# Permite modificar uma variável global dentro da função.
# Allows modifying a global variable inside a function.
#
# OPERAÇÕES / OPERATIONS:
#
# diameter += 10
# Soma 10 ao valor atual.
# Adds 10 to the current value.
#
# diameter -= 10
# Subtrai 10 do valor atual.
# Subtracts 10 from the current value.
#
# diameter *= 2
# Multiplica o valor por 2.
# Multiplies the value by 2.
#
# CONDIÇÕES / CONDITIONS:
#
# if condição:
# Executa se for verdadeiro.
# Executes if true.
#
# else:
# Executa se o IF for falso.
# Executes if IF is false.
#
# OPERADORES DE COMPARAÇÃO / COMPARISON OPERATORS:
#
# ==  Igual a / Equal to
# !=  Diferente de / Not equal to
# >   Maior que / Greater than
# <   Menor que / Less than
# >=  Maior ou igual / Greater than or equal to
# <=  Menor ou igual / Less than or equal to
#
# TURTLE GRÁFICO / GRAPHICS:
#
# color("purple")
# Define uma cor.
# Sets a color.
#
# dot(40)
# Desenha um círculo preenchido.
# Draws a filled circle.
#
# clear()
# Apaga os desenhos.
# Clears drawings.
#
# write("Olá!")
# Escreve um texto na tela.
# Writes text on the screen.
#
# EVENTOS / EVENTS:
#
# Screen()
# Acessa a janela.
# Accesses the screen.
#
# screen.listen()
# Ativa a escuta do teclado.
# Activates keyboard listening.
#
# screen.onkey(funcao, "Up")
# Associa uma tecla a uma função.
# Connects a key to a function.
#
# done()
# Mantém a janela aberta.
# Keeps the window open.
#
# ================================================================
# 9. CONCEITOS IMPORTANTES DESTE PROJETO
# IMPORTANT CONCEPTS IN THIS PROJECT
# ================================================================
#
# 1. VARIÁVEIS:
# Guardam valores que podem mudar.
# Store values that can change.
#
# 2. FUNÇÕES:
# Organizam o código em blocos reutilizáveis.
# Organize code into reusable blocks.
#
# 3. GLOBAL:
# Permite modificar variáveis globais dentro de funções.
# Allows modifying global variables inside functions.
#
# 4. CONDIÇÕES:
# Permitem tomar decisões no programa.
# Allow programs to make decisions.
#
# 5. EVENTOS:
# Permitem executar funções em resposta ao teclado.
# Allow functions to run in response to keyboard input.
#
# 6. BIBLIOTECA TURTLE:
# Permite criar desenhos, gráficos e pequenas animações.
# Allows creating drawings, graphics and small animations.
#
# ================================================================
# FIM DO GUIA / END OF GUIDE
# ================================================================
