
# ============================================================
# PYTHON PLAYGROUND #1
# EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ============================================================
#
# Conteúdos / Topics:
# 1. Condicionais / Conditionals
# 2. Funções / Functions
# 3. Listas e ordenação / Lists and sorting
# 4. Matemática / Mathematics
# 5. Números primos / Prime numbers
# 6. Strings e vogais / Strings and vowels
# 7. List comprehension / Compreensão de listas
# 8. Operadores matemáticos / Mathematical operators
# 9. Manipulação de strings / String manipulation
# 10. Loops e fatorial / Loops and factorial
#
# ============================================================


# ============================================================
# EXERCÍCIO 1 - NÚMERO POSITIVO, NEGATIVO OU ZERO
# EXERCISE 1 - POSITIVE, NEGATIVE OR ZERO
# ============================================================

# Verifique se um número é positivo, negativo ou zero.
# Check whether a number is positive, negative or zero.

number = -10

if number > 0:
    print("Exercício 1: Número positivo / Positive number")

elif number < 0:
    print("Exercício 1: Número negativo / Negative number")

else:
    print("Exercício 1: O número é zero / The number is zero")


# Explicação / Explanation:
#
# if:
# Verifica se uma condição é verdadeira.
# Checks whether a condition is true.
#
# elif:
# Verifica outra condição caso a anterior seja falsa.
# Checks another condition if the previous one is false.
#
# else:
# Executa quando nenhuma condição anterior é verdadeira.
# Executes when no previous condition is true.
#
# >  Maior que / Greater than
# <  Menor que / Less than


# ============================================================
# EXERCÍCIO 2 - MÁXIMO ENTRE TRÊS NÚMEROS
# EXERCISE 2 - MAXIMUM OF THREE NUMBERS
# ============================================================

# Crie uma função que calcule o máximo entre três números.
# Create a function that calculates the maximum of three numbers.

def maximum_of_three(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


result = maximum_of_three(15, 40, 25)

print("\nExercício 2: Maior número / Largest number:", result)


# Explicação / Explanation:
#
# def:
# Cria uma função.
# Defines a function.
#
# return:
# Retorna o resultado da função.
# Returns the function result.
#
# and:
# Operador lógico E.
# Logical AND operator.
#
# >=:
# Maior ou igual.
# Greater than or equal to.


# ============================================================
# EXERCÍCIO 3 - LISTA EM ORDEM ALFABÉTICA
# EXERCISE 3 - ALPHABETICAL LIST
# ============================================================

# Crie uma lista de nomes e ordene em ordem alfabética.
# Create a list of names and sort them alphabetically.

names = [
    "Carlos",
    "Ana",
    "Pedro",
    "Beatriz",
    "Lucas",
    "Fernanda"
]

sorted_names = sorted(names)

print("\nExercício 3: Nomes em ordem alfabética:")
print(sorted_names)


# Explicação / Explanation:
#
# []:
# Cria uma lista.
# Creates a list.
#
# sorted():
# Retorna uma nova lista ordenada.
# Returns a new sorted list.
#
# print():
# Exibe informações na tela.
# Displays information on the screen.
#
# IMPORTANTE / IMPORTANT:
# sorted() não modifica a lista original.
# sorted() does not modify the original list.


# ============================================================
# EXERCÍCIO 4 - ÁREA DE UM CÍRCULO
# EXERCISE 4 - AREA OF A CIRCLE
# ============================================================

# Calcule a área de um círculo.
# Calculate the area of a circle.
#
# Fórmula / Formula:
# A = π * r²

import math

radius = 5

def calculate_circle_area(radius):

    area = math.pi * radius ** 2

    return area


area = calculate_circle_area(radius)

print("\nExercício 4: Área do círculo / Circle area:")
print(round(area, 2))


# Explicação / Explanation:
#
# import math:
# Importa a biblioteca matemática.
# Imports the mathematics library.
#
# math.pi:
# Representa o número π.
# Represents the number π.
#
# **:
# Operador de potência.
# Exponentiation operator.
#
# round(valor, 2):
# Arredonda o resultado para duas casas decimais.
# Rounds the result to two decimal places.


# ============================================================
# EXERCÍCIO 5 - VERIFICAR SE UM NÚMERO É PRIMO
# EXERCISE 5 - CHECK IF A NUMBER IS PRIME
# ============================================================

# Crie uma função que verifique se um número é primo.
# Create a function that checks whether a number is prime.
#
# Número primo:
# É divisível somente por 1 e por ele mesmo.
#
# Prime number:
# Is divisible only by 1 and itself.

def is_prime(number):

    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            return False

    return True


number = 17

if is_prime(number):
    print("\nExercício 5:", number, "é primo / is prime")

else:
    print("\nExercício 5:", number, "não é primo / is not prime")


# Explicação / Explanation:
#
# for:
# Cria um loop para percorrer valores.
# Creates a loop to iterate through values.
#
# range(inicio, fim):
# Gera uma sequência de números.
# Generates a sequence of numbers.
#
# %:
# Operador de módulo: retorna o resto da divisão.
# Modulo operator: returns the remainder of a division.
#
# ==:
# Verifica se dois valores são iguais.
# Checks whether two values are equal.
#
# return False:
# Retorna falso.
# Returns false.
#
# return True:
# Retorna verdadeiro.
# Returns true.
#
# Se o resto da divisão for zero, encontramos um divisor.
# If the remainder is zero, we found a divisor.


# ============================================================
# EXERCÍCIO 6 - CONTAR VOGAIS
# EXERCISE 6 - COUNT VOWELS
# ============================================================

# Crie um programa que conte o número de vogais em uma palavra.
# Create a program that counts the vowels in a word.

def count_vowels(word):

    vowels = "aeiouáéíóúâêôãõ"

    total = 0

    for letter in word.lower():

        if letter in vowels:
            total += 1

    return total


word = "Programacao Python"

result = count_vowels(word)

print("\nExercício 6: Palavra / Word:", word)
print("Quantidade de vogais / Number of vowels:", result)


# Explicação / Explanation:
#
# .lower():
# Converte o texto para letras minúsculas.
# Converts text to lowercase.
#
# in:
# Verifica se um elemento está dentro de uma sequência.
# Checks whether an element belongs to a sequence.
#
# total += 1:
# Incrementa o contador em uma unidade.
# Increases the counter by one.


# ============================================================
# EXERCÍCIO 7 - NÚMEROS PARES DE 1 A 20
# EXERCISE 7 - EVEN NUMBERS FROM 1 TO 20
# ============================================================

# Crie uma lista com os números pares de 1 a 20.
# Create a list with even numbers from 1 to 20.

even_numbers = [
    number
    for number in range(1, 21)
    if number % 2 == 0
]

print("\nExercício 7: Números pares / Even numbers:")
print(even_numbers)


# Explicação / Explanation:
#
# List comprehension:
# Forma resumida de criar listas.
# A shorter way to create lists.
#
# range(1, 21):
# Gera números de 1 até 20.
# Generates numbers from 1 to 20.
#
# number % 2 == 0:
# Verifica se o número é divisível por 2.
# Checks whether the number is divisible by 2.
#
# Se o resto for zero, o número é par.
# If the remainder is zero, the number is even.


# ============================================================
# EXERCÍCIO 8 - QUADRADO DE UM NÚMERO
# EXERCISE 8 - SQUARE OF A NUMBER
# ============================================================

# Crie uma função que calcule o quadrado de um número.
# Create a function that calculates the square of a number.

def calculate_square(number):

    return number ** 2


result = calculate_square(8)

print("\nExercício 8: Quadrado de 8 / Square of 8:", result)


# Explicação / Explanation:
#
# ** 2:
# Eleva o número ao quadrado.
# Raises the number to the power of two.
#
# Exemplo / Example:
# 8 ** 2 = 64
#
# return:
# Devolve o resultado da função.
# Returns the function result.


# ============================================================
# EXERCÍCIO 9 - CONTAR PALAVRAS DE UMA FRASE
# EXERCISE 9 - COUNT WORDS IN A SENTENCE
# ============================================================

# Crie um programa que leia uma frase e conte o número de palavras.
# Create a program that reads a sentence and counts its words.

def count_words(sentence):

    words = sentence.split()

    return len(words)


sentence = "Estou aprendendo Python todos os dias"

result = count_words(sentence)

print("\nExercício 9: Frase / Sentence:", sentence)
print("Quantidade de palavras / Number of words:", result)


# Explicação / Explanation:
#
# .split():
# Divide uma string em uma lista de palavras.
# Splits a string into a list of words.
#
# len():
# Retorna a quantidade de elementos.
# Returns the number of elements.
#
# Exemplo / Example:
# "Olá mundo Python".split()
# Resultado / Result:
# ["Olá", "mundo", "Python"]
#
# len(["Olá", "mundo", "Python"]) = 3


# ============================================================
# EXERCÍCIO 10 - FATORIAL COM LOOP
# EXERCISE 10 - FACTORIAL USING A LOOP
# ============================================================

# Crie um programa que calcule o fatorial de um número usando um loop.
# Create a program that calculates the factorial of a number using a loop.
#
# Exemplo / Example:
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def calculate_factorial(number):

    if number < 0:
        raise ValueError("O fatorial não existe para números negativos.")

    factorial = 1

    for value in range(1, number + 1):

        factorial *= value

    return factorial


number = 5

result = calculate_factorial(number)

print("\nExercício 10: Fatorial de", number, "/ Factorial of", number)
print(result)


# Explicação / Explanation:
#
# factorial = 1:
# Inicializa o acumulador.
# Initializes the accumulator.
#
# for:
# Percorre os números da sequência.
# Iterates through the sequence.
#
# range(1, number + 1):
# Gera números de 1 até o número informado.
# Generates numbers from 1 up to the given number.
#
# *=:
# Multiplica o valor atual e atualiza a variável.
# Multiplies the current value and updates the variable.
#
# raise ValueError:
# Lança um erro quando recebemos um valor inválido.
# Raises an error when we receive an invalid value.
#
# OBSERVAÇÃO / NOTE:
# O fatorial de zero é 1.
# The factorial of zero is 1.
#
# ============================================================
# FIM DO PYTHON PLAYGROUND #1
# END OF PYTHON PLAYGROUND #1
# ============================================================
