
# ============================================================
# EXERCÍCIO 1: CONTAGEM REGRESSIVA
# EXERCISE 1: COUNTDOWN
# ============================================================

# Solicita um número positivo ao usuário.
# Requests a positive number from the user.
numero = int(input("Digite um número positivo / Enter a positive number: "))

# Verifica se o número é positivo.
# Checks whether the number is positive.
while numero < 0:
    print("Número inválido! Digite um número positivo.")
    numero = int(input("Enter a positive number: "))

# Realiza a contagem regressiva até zero.
# Performs the countdown until zero.
while numero >= 0:
    print(numero)
    numero -= 1

print("Contagem finalizada! / Countdown finished!")


# ============================================================
# EXERCÍCIO 2: ADIVINHE O NÚMERO
# EXERCISE 2: GUESS THE NUMBER
# ============================================================

# Importa o módulo random para gerar números aleatórios.
# Imports the random module to generate random numbers.
import random

# Gera um número aleatório entre 1 e 100.
# Generates a random number between 1 and 100.
numero_secreto = random.randint(1, 100)

# Inicializa a variável do palpite.
# Initializes the guess variable.
palpite = 0

print("Tente adivinhar o número entre 1 e 100!")
print("Try to guess the number between 1 and 100!")

# Continua solicitando palpites até acertar.
# Keeps requesting guesses until the user gets it right.
while palpite != numero_secreto:

    palpite = int(input("Digite seu palpite / Enter your guess: "))

    if palpite < numero_secreto:
        print("O número secreto é MAIOR! / The secret number is HIGHER!")

    elif palpite > numero_secreto:
        print("O número secreto é MENOR! / The secret number is LOWER!")

    else:
        print("Parabéns! Você acertou! / Congratulations! You guessed it!")

print("Número secreto:", numero_secreto)


# ============================================================
# EXERCÍCIO 3: CALCULADORA SIMPLES
# EXERCISE 3: SIMPLE CALCULATOR
# ============================================================

# Inicializa a opção do usuário.
# Initializes the user's option.
opcao = ""

# O menu continua aparecendo até o usuário escolher sair.
# The menu keeps appearing until the user chooses to exit.
while opcao != "5":

    print("\n========== CALCULADORA / CALCULATOR ==========")
    print("1 - Adição / Addition")
    print("2 - Subtração / Subtraction")
    print("3 - Multiplicação / Multiplication")
    print("4 - Divisão / Division")
    print("5 - Sair / Exit")

    opcao = input("Escolha uma operação / Choose an operation: ")

    # Verifica se o usuário deseja sair.
    # Checks whether the user wants to exit.
    if opcao == "5":
        print("Calculadora encerrada! / Calculator closed!")

    # Verifica se a opção escolhida é válida.
    # Checks whether the selected option is valid.
    elif opcao in ["1", "2", "3", "4"]:

        # Solicita os dois números.
        # Requests the two numbers.
        numero1 = float(input("Digite o primeiro número / Enter the first number: "))
        numero2 = float(input("Digite o segundo número / Enter the second number: "))

        # ADIÇÃO / ADDITION
        if opcao == "1":
            resultado = numero1 + numero2
            print("Resultado da adição / Addition result:", resultado)

        # SUBTRAÇÃO / SUBTRACTION
        elif opcao == "2":
            resultado = numero1 - numero2
            print("Resultado da subtração / Subtraction result:", resultado)

        # MULTIPLICAÇÃO / MULTIPLICATION
        elif opcao == "3":
            resultado = numero1 * numero2
            print("Resultado da multiplicação / Multiplication result:", resultado)

        # DIVISÃO / DIVISION
        elif opcao == "4":

            # Evita divisão por zero.
            # Prevents division by zero.
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado da divisão / Division result:", resultado)
            else:
                print("Erro: divisão por zero não é permitida!")
                print("Error: division by zero is not allowed!")

    else:
        print("Opção inválida! Tente novamente.")
        print("Invalid option! Try again.")


# ============================================================
# FIM DOS EXERCÍCIOS / END OF EXERCISES
# ============================================================
