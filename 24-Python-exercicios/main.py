
# ============================================================
# EXERCÍCIO 1: CALCULADORA SIMPLES
# EXERCISE 1: SIMPLE CALCULATOR
# ============================================================

# Cria uma função que recebe dois números e uma operação.
# Creates a function that receives two numbers and an operation.

def calculadora(numero1, numero2, operacao):

    # Verifica qual operação foi escolhida.
    # Checks which operation was selected.

    if operacao == "soma":
        return numero1 + numero2

    elif operacao == "subtracao":
        return numero1 - numero2

    elif operacao == "multiplicacao":
        return numero1 * numero2

    elif operacao == "divisao":

        # Verifica se o segundo número é diferente de zero.
        # Checks whether the second number is different from zero.

        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: divisão por zero não permitida."

    else:
        return "Operação inválida."


# Chamando a função / Calling the function

print("Soma:", calculadora(10, 5, "soma"))
print("Subtração:", calculadora(10, 5, "subtracao"))
print("Multiplicação:", calculadora(10, 5, "multiplicacao"))
print("Divisão:", calculadora(10, 5, "divisao"))
print("Divisão por zero:", calculadora(10, 0, "divisao"))


# ============================================================
# EXERCÍCIO 2: VERIFICAR NÚMERO PRIMO
# EXERCISE 2: CHECK PRIME NUMBER
# ============================================================

# Cria uma função que recebe um número inteiro.
# Creates a function that receives an integer.

def eh_primo(numero):

    # Números menores que 2 não são primos.
    # Numbers smaller than 2 are not prime.

    if numero < 2:
        return False

    # Verifica se o número possui algum divisor.
    # Checks whether the number has any divisor.

    for divisor in range(2, numero):

        if numero % divisor == 0:
            return False

    # Se não encontrou divisores, o número é primo.
    # If no divisors were found, the number is prime.

    return True


# Chamando a função / Calling the function

print("Número 7:", eh_primo(7))
print("Número 10:", eh_primo(10))
print("Número 2:", eh_primo(2))
print("Número 1:", eh_primo(1))
print("Número 17:", eh_primo(17))


# ============================================================
# EXERCÍCIO 3: CONTAGEM DE VOGAIS
# EXERCISE 3: COUNT VOWELS
# ============================================================

# Cria uma função que recebe uma string.
# Creates a function that receives a string.

def contar_vogais(texto):

    # Define as vogais.
    # Defines the vowels.

    vogais = "aeiou"

    # Inicializa o contador.
    # Initializes the counter.

    contador = 0

    # Percorre cada letra da string.
    # Iterates through each letter of the string.

    for letra in texto:

        # Converte a letra para minúscula e verifica se é vogal.
        # Converts the letter to lowercase and checks if it is a vowel.

        if letra.lower() in vogais:
            contador += 1

    # Retorna a quantidade total de vogais.
    # Returns the total number of vowels.

    return contador


# Chamando a função / Calling the function

print("Vogais em Python:", contar_vogais("Python"))
print("Vogais em Programação:", contar_vogais("Programação"))
print("Vogais em ENZzO:", contar_vogais("ENZzO"))
print("Vogais em Hello World:", contar_vogais("Hello World"))


# ============================================================
# FIM DOS EXERCÍCIOS / END OF EXERCISES
# ============================================================
