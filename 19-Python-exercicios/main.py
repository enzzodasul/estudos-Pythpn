
# ============================================================
# EXERCÍCIO 1: VERIFICAÇÃO DE NÚMERO PAR OU ÍMPAR
# EXERCISE 1: CHECK IF A NUMBER IS EVEN OR ODD
# ============================================================

# Solicita um número inteiro ao usuário.
# Requests an integer from the user.
numero = int(input("Digite um número inteiro / Enter an integer: "))

# Verifica se o resto da divisão por 2 é igual a zero.
# Checks whether the remainder of division by 2 is zero.
if numero % 2 == 0:
    print("O número é PAR / The number is EVEN")
else:
    print("O número é ÍMPAR / The number is ODD")


# ============================================================
# EXERCÍCIO 2: CLASSIFICAÇÃO DE IDADE
# EXERCISE 2: AGE CLASSIFICATION
# ============================================================

# Solicita a idade do usuário.
# Requests the user's age.
idade = int(input("Digite sua idade / Enter your age: "))

# Classifica a idade de acordo com as condições.
# Classifies the age according to the conditions.
if idade < 0:
    print("Idade inválida / Invalid age")
elif idade <= 12:
    print("Criança / Child")
elif idade <= 17:
    print("Adolescente / Teenager")
else:
    print("Adulto / Adult")


# ============================================================
# EXERCÍCIO 3: CALCULADORA DE IMC COM CLASSIFICAÇÃO
# EXERCISE 3: BMI CALCULATOR WITH CLASSIFICATION
# ============================================================

# Solicita o peso e a altura do usuário.
# Requests the user's weight and height.
peso = float(input("Digite seu peso em kg / Enter your weight in kg: "))
altura = float(input("Digite sua altura em metros / Enter your height in meters: "))

# Verifica se os valores são válidos.
# Checks whether the values are valid.
if peso <= 0 or altura <= 0:
    print("Peso ou altura inválidos / Invalid weight or height")

else:
    # Calcula o IMC.
    # Calculates the BMI.
    imc = peso / (altura ** 2)

    # Exibe o resultado do IMC.
    # Displays the BMI result.
    print(f"Seu IMC é: {imc:.2f} / Your BMI is: {imc:.2f}")

    # Classifica o resultado.
    # Classifies the result.
    if imc < 18.5:
        print("Abaixo do peso / Underweight")
    elif imc < 25:
        print("Peso normal / Normal weight")
    else:
        print("Acima do peso / Overweight")


# ============================================================
# FIM DOS EXERCÍCIOS / END OF EXERCISES
# ============================================================
