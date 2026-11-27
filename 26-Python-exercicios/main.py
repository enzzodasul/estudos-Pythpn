
# ============================================================
# EXERCÍCIO 1: FUNÇÃO LAMBDA PARA CALCULAR O QUADRADO
# EXERCISE 1: LAMBDA FUNCTION TO CALCULATE THE SQUARE
# ============================================================

# PT: Crie uma função lambda que receba um número
# e retorne o quadrado desse número.
#
# EN: Create a lambda function that receives a number
# and returns its square.

quadrado = lambda numero: numero ** 2

print(quadrado(5))  # Resultado / Output: 25
print(quadrado(8))  # Resultado / Output: 64


# ============================================================
# EXERCÍCIO 2: FUNÇÃO COM RETORNO MÚLTIPLO
# EXERCISE 2: FUNCTION WITH MULTIPLE RETURN VALUES
# ============================================================

# PT: Crie uma função chamada calcula_dobro_e_triplo
# que receba um número e retorne seu dobro e triplo.
#
# EN: Create a function called calcula_dobro_e_triplo
# that receives a number and returns its double and triple.

def calcula_dobro_e_triplo(numero):

    dobro = numero * 2
    triplo = numero * 3

    return dobro, triplo


# Recebendo os dois valores / Receiving both values
resultado_dobro, resultado_triplo = calcula_dobro_e_triplo(10)

print("Dobro:", resultado_dobro)    # 20
print("Triplo:", resultado_triplo)  # 30


# Outra maneira de utilizar / Another way to use it
print(calcula_dobro_e_triplo(5))  # (10, 15)


# ============================================================
# EXERCÍCIO 3: ORDENAÇÃO COM FUNÇÃO LAMBDA
# EXERCISE 3: SORTING WITH A LAMBDA FUNCTION
# ============================================================

# PT: Crie uma lista de números e ordene-a
# em ordem crescente usando uma função lambda.
#
# EN: Create a list of numbers and sort it
# in ascending order using a lambda function.

numeros = [8, 3, 10, 1, 7, 5, 2, 9, 4, 6]

numeros_ordenados = sorted(numeros, key=lambda numero: numero)

print("Lista original:", numeros)
print("Lista ordenada:", numeros_ordenados)

# Resultado / Output:
# Lista original: [8, 3, 10, 1, 7, 5, 2, 9, 4, 6]
# Lista ordenada: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# lambda:
# PT: Cria uma função anônima.
# EN: Creates an anonymous function.

# ** 2:
# PT: Calcula o quadrado de um número.
# EN: Calculates the square of a number.

# return dobro, triplo:
# PT: Retorna dois valores em uma tupla.
# EN: Returns two values in a tuple.

# sorted():
# PT: Cria uma nova lista ordenada.
# EN: Creates a new sorted list.

# key=lambda numero: numero:
# PT: Define o critério de ordenação.
# EN: Defines the sorting criterion.
