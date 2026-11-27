
# ============================================================
# PYTHON - INTRODUÇÃO ÀS FUNÇÕES
# PYTHON - INTRODUCTION TO FUNCTIONS
# ============================================================

# 1. O QUE SÃO FUNÇÕES? / WHAT ARE FUNCTIONS?
#
# Funções são blocos de código que executam tarefas específicas.
# Functions are blocks of code that perform specific tasks.
#
# Elas permitem reutilizar códigos sem precisar escrevê-los novamente.
# They allow us to reuse code without writing it again.


# 2. COMO CRIAR UMA FUNÇÃO / HOW TO CREATE A FUNCTION
#
# Utilizamos a palavra-chave def.
# We use the def keyword.

def saudacao():
    print("Olá! Seja bem-vindo ao Python!")
    print("Hello! Welcome to Python!")


# 3. COMO CHAMAR UMA FUNÇÃO / HOW TO CALL A FUNCTION
#
# Para executar uma função, precisamos chamá-la pelo nome.
# To execute a function, we need to call it by its name.

def mensagem():
    print("Estou aprendendo funções!")
    print("I am learning functions!")

mensagem()


# 4. FUNÇÃO SEM PARÂMETROS / FUNCTION WITHOUT PARAMETERS

def apresentar():
    print("Meu nome é Enzo.")
    print("I am Enzo.")

apresentar()


# 5. FUNÇÃO COM PARÂMETROS / FUNCTION WITH PARAMETERS
#
# Parâmetros são variáveis recebidas pela função.
# Parameters are variables received by a function.

def saudacao_personalizada(nome):
    print(f"Olá, {nome}!")
    print(f"Hello, {nome}!")

saudacao_personalizada("Enzo")
saudacao_personalizada("Carlos")


# 6. FUNÇÃO COM DOIS PARÂMETROS
# FUNCTION WITH TWO PARAMETERS

def apresentar_pessoa(nome, idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar_pessoa("Enzo", 20)


# 7. PARÂMETROS E ARGUMENTOS
# PARAMETERS AND ARGUMENTS
#
# Parâmetro: variável declarada na definição da função.
# Parameter: variable declared in the function definition.
#
# Argumento: valor enviado ao chamar a função.
# Argument: value passed when calling the function.

def mostrar_nome(nome):  # nome = parâmetro / parameter
    print(nome)

mostrar_nome("Enzo")  # "Enzo" = argumento / argument


# 8. FUNÇÃO COM RETURN
# FUNCTION WITH RETURN
#
# O return devolve um resultado da função.
# Return sends a result back from the function.

def somar(a, b):
    return a + b

resultado = somar(10, 5)

print("Resultado:", resultado)


# 9. DIFERENÇA ENTRE PRINT E RETURN
# DIFFERENCE BETWEEN PRINT AND RETURN

# PRINT apenas exibe uma informação.
# PRINT only displays information.

def mostrar_mensagem():
    print("Olá!")

mostrar_mensagem()


# RETURN devolve um valor que pode ser utilizado depois.
# RETURN returns a value that can be used later.

def calcular():
    return 10 + 20

resultado = calcular()

print(resultado)


# 10. FUNÇÃO COM OPERAÇÕES MATEMÁTICAS
# FUNCTION WITH MATHEMATICAL OPERATIONS

def multiplicar(a, b):
    return a * b

resultado = multiplicar(5, 4)

print("Multiplicação:", resultado)


# 11. PARÂMETROS COM VALORES PADRÃO
# PARAMETERS WITH DEFAULT VALUES
#
# Um valor padrão é utilizado quando nenhum argumento é informado.
# A default value is used when no argument is provided.

def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao()
saudacao("Enzo")


# 12. ARGUMENTOS NOMEADOS
# KEYWORD ARGUMENTS
#
# Podemos informar o nome do parâmetro ao chamar a função.
# We can specify the parameter name when calling the function.

def cadastrar_pessoa(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)

cadastrar_pessoa(nome="Enzo", idade=20)
cadastrar_pessoa(idade=25, nome="Carlos")


# 13. FUNÇÃO COM IF E ELSE
# FUNCTION WITH IF AND ELSE

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade / Adult"
    else:
        return "Menor de idade / Minor"

print(verificar_idade(20))
print(verificar_idade(15))


# 14. FUNÇÃO COM FOR
# FUNCTION WITH FOR

def mostrar_numeros():
    for numero in range(1, 6):
        print(numero)

mostrar_numeros()


# 15. FUNÇÃO COM WHILE
# FUNCTION WITH WHILE

def contagem_regressiva(numero):
    while numero >= 0:
        print(numero)
        numero -= 1

contagem_regressiva(5)


# 16. FUNÇÃO COM LISTAS
# FUNCTION WITH LISTS

def mostrar_frutas(frutas):
    for fruta in frutas:
        print(fruta)

lista_frutas = ["Maçã", "Banana", "Uva"]

mostrar_frutas(lista_frutas)


# 17. FUNÇÃO QUE RETORNA UMA LISTA
# FUNCTION THAT RETURNS A LIST

def criar_lista():
    numeros = [10, 20, 30, 40, 50]
    return numeros

resultado = criar_lista()

print(resultado)


# 18. FUNÇÃO COM MAIS DE UM RETURN
# FUNCTION WITH MORE THAN ONE RETURN

def classificar_nota(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

print(classificar_nota(8))
print(classificar_nota(6))
print(classificar_nota(3))


# 19. FUNÇÃO COM INPUT
# FUNCTION WITH INPUT

def perguntar_nome():
    nome = input("Digite seu nome / Enter your name: ")
    print(f"Olá, {nome}!")

perguntar_nome()


# 20. FUNÇÕES COM VÁRIOS PARÂMETROS
# FUNCTIONS WITH MULTIPLE PARAMETERS

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(8, 7, 9)

print(f"Média: {resultado:.2f}")


# 21. FUNÇÃO COM *ARGS
# FUNCTION WITH *ARGS
#
# Permite receber uma quantidade variável de argumentos posicionais.
# Allows receiving a variable number of positional arguments.

def somar_varios(*numeros):
    return sum(numeros)

print(somar_varios(10, 20))
print(somar_varios(10, 20, 30, 40))


# 22. FUNÇÃO COM **KWARGS
# FUNCTION WITH **KWARGS
#
# Permite receber vários argumentos nomeados.
# Allows receiving multiple keyword arguments.

def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(chave, ":", valor)

mostrar_dados(nome="Enzo", idade=20, cidade="Juiz de Fora")


# 23. ESCOPO DE VARIÁVEIS
# VARIABLE SCOPE
#
# Variável local: existe dentro da função.
# Local variable: exists inside the function.
#
# Variável global: pode ser acessada em diferentes partes do programa.
# Global variable: can be accessed in different parts of the program.

nome = "Enzo"  # Variável global / Global variable

def mostrar():
    idade = 20  # Variável local / Local variable
    print(nome)
    print(idade)

mostrar()


# 24. DOCSTRING
# DOCUMENTAÇÃO DE FUNÇÕES / FUNCTION DOCUMENTATION
#
# Docstrings documentam o objetivo de uma função.
# Docstrings describe the purpose of a function.

def dividir(a, b):
    """
    Divide dois números.
    Divides two numbers.
    """
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

print(dividir(10, 2))


# 25. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Crie uma função que exiba uma mensagem de boas-vindas.
# Create a function that displays a welcome message.

def boas_vindas():
    print("Bem-vindo ao Python!")
    print("Welcome to Python!")

boas_vindas()


# EXERCÍCIO 2 / EXERCISE 2
# Crie uma função que receba dois números e retorne a soma.
# Create a function that receives two numbers and returns the sum.

def somar(a, b):
    return a + b

print("Soma:", somar(10, 20))


# EXERCÍCIO 3 / EXERCISE 3
# Crie uma função que verifique se um número é par ou ímpar.
# Create a function that checks whether a number is even or odd.

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par / Even"
    else:
        return "Ímpar / Odd"

print(verificar_par_impar(10))
print(verificar_par_impar(7))


# EXERCÍCIO 4 / EXERCISE 4
# Crie uma função que calcule a média de duas notas.
# Create a function that calculates the average of two grades.

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

print("Média:", calcular_media(8, 10))


# EXERCÍCIO 5 / EXERCISE 5
# Crie uma função que receba um nome e uma idade.
# Create a function that receives a name and an age.

def apresentar(nome, idade):
    print(f"Meu nome é {nome} e tenho {idade} anos.")

apresentar("Enzo", 20)


# ============================================================
# 26. EXERCÍCIOS PARA PRATICAR / PRACTICE EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Crie uma função chamada mensagem que exiba "Olá, mundo!".
# Create a function called mensagem that displays "Hello, world!".


# EXERCÍCIO 2 / EXERCISE 2
# Crie uma função que receba três números e retorne a soma.
# Create a function that receives three numbers and returns their sum.


# EXERCÍCIO 3 / EXERCISE 3
# Crie uma função que receba um número e retorne seu quadrado.
# Create a function that receives a number and returns its square.


# EXERCÍCIO 4 / EXERCISE 4
# Crie uma função que receba uma idade e informe se é maior de idade.
# Create a function that receives an age and checks if the person is an adult.


# EXERCÍCIO 5 / EXERCISE 5
# Crie uma função que receba uma lista de números e retorne a soma.
# Create a function that receives a list of numbers and returns their sum.


# EXERCÍCIO 6 / EXERCISE 6
# Crie uma função que receba uma palavra e conte suas letras.
# Create a function that receives a word and counts its letters.


# ============================================================
# 27. RESUMO / SUMMARY
# ============================================================

# def       = cria uma função / defines a function
# return    = retorna um resultado / returns a result
# print()   = exibe uma informação / displays information
# input()   = recebe dados do usuário / receives user input
# parâmetros = variáveis declaradas na função / function variables
# argumentos = valores enviados à função / values passed to a function
# *args     = recebe vários argumentos posicionais / multiple positional arguments
# **kwargs  = recebe vários argumentos nomeados / multiple keyword arguments
# docstring = documenta uma função / documents a function
#
# IMPORTANTE / IMPORTANT:
# Criar uma função não significa executá-la.
# Defining a function does not mean executing it.
#
# Para executar, precisamos chamar a função.
# To execute it, we need to call the function.
#
# ============================================================
# FIM DO MATERIAL / END OF MATERIAL
# ============================================================
