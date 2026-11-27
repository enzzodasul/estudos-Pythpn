
# ============================================================
# EXERCÍCIO 1: CRIAR UMA TUPLA
# EXERCISE 1: CREATE A TUPLE
# ============================================================
#
# Crie uma tupla com nomes de três cores de sua escolha
# e exiba-a na tela.
#
# Create a tuple with three colors of your choice
# and display it on the screen.

cores = ("Azul", "Verde", "Vermelho")

print("Exercício 1 - Cores:")
print(cores)


# ============================================================
# EXERCÍCIO 2: ACESSAR ELEMENTOS
# EXERCISE 2: ACCESS ELEMENTS
# ============================================================
#
# Dada uma tupla de números, acesse o terceiro elemento
# e exiba-o.
#
# Given a tuple of numbers, access the third element
# and display it.
#
# IMPORTANTE:
# O primeiro índice é 0.
# O segundo índice é 1.
# O terceiro índice é 2.
#
# IMPORTANT:
# The first index is 0.
# The second index is 1.
# The third index is 2.

numeros = (10, 20, 30, 40, 50)

terceiro_elemento = numeros[2]

print("\nExercício 2 - Terceiro elemento:")
print(terceiro_elemento)


# ============================================================
# EXERCÍCIO 3: CONCATENAR TUPLAS
# EXERCISE 3: CONCATENATE TUPLES
# ============================================================
#
# Crie duas tuplas com números e depois crie uma terceira
# tupla que seja a concatenação das duas.
#
# Create two tuples with numbers and then create a third
# tuple that concatenates both.
#
# O operador + une duas tuplas.
# The + operator joins two tuples.

tupla1 = (1, 2, 3)

tupla2 = (4, 5, 6)

tupla3 = tupla1 + tupla2

print("\nExercício 3 - Concatenação:")
print("Primeira tupla:", tupla1)
print("Segunda tupla:", tupla2)
print("Terceira tupla:", tupla3)


# ============================================================
# RESUMO DOS RESULTADOS
# SUMMARY OF RESULTS
# ============================================================
#
# Exercício 1: ('Azul', 'Verde', 'Vermelho')
# Exercício 2: 30
# Exercício 3: (1, 2, 3, 4, 5, 6)
