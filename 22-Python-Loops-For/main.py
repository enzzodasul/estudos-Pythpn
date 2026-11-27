
# ============================================================
# PYTHON - FOR
# PYTHON - FOR LOOPS
# ============================================================

# 1. O QUE É FOR? / WHAT IS FOR?
# O for percorre uma sequência de elementos.
# The for loop iterates through a sequence of elements.

for numero in range(5):
    print(numero)

# Resultado / Output:
# 0
# 1
# 2
# 3
# 4


# 2. SINTAXE DO FOR / FOR SYNTAX

# for variável in sequência:
#     código que será repetido
#
# for variable in sequence:
#     code that will be repeated


# 3. FOR COM RANGE()
# RANGE() GENERATES A SEQUENCE OF NUMBERS

# range(5) gera números de 0 até 4.
# range(5) generates numbers from 0 to 4.

for numero in range(5):
    print(numero)


# 4. RANGE COM INÍCIO E FIM
# RANGE WITH START AND END

# range(1, 6) gera números de 1 até 5.
# range(1, 6) generates numbers from 1 to 5.

for numero in range(1, 6):
    print(numero)


# 5. RANGE COM PASSO
# RANGE WITH STEP

# O terceiro argumento define o intervalo entre os números.
# The third argument defines the interval between numbers.

for numero in range(0, 11, 2):
    print(numero)

# Resultado / Output:
# 0, 2, 4, 6, 8, 10


# 6. CONTAGEM REGRESSIVA
# COUNTDOWN

for numero in range(10, 0, -1):
    print(numero)

print("Fim! / Finished!")


# 7. FOR COM STRINGS
# FOR WITH STRINGS

nome = "Python"

for letra in nome:
    print(letra)

# Cada letra é exibida individualmente.
# Each letter is displayed individually.


# 8. FOR COM LISTAS
# FOR WITH LISTS

frutas = ["Maçã", "Banana", "Uva", "Morango"]

for fruta in frutas:
    print(fruta)


# 9. FOR COM TUPLAS
# FOR WITH TUPLES

cores = ("Azul", "Verde", "Vermelho")

for cor in cores:
    print(cor)


# 10. FOR COM DICIONÁRIOS
# FOR WITH DICTIONARIES

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Juiz de Fora"
}

# Percorrendo as chaves.
# Iterating through keys.

for chave in pessoa:
    print(chave)

# Percorrendo os valores.
# Iterating through values.

for valor in pessoa.values():
    print(valor)

# Percorrendo chaves e valores.
# Iterating through keys and values.

for chave, valor in pessoa.items():
    print(chave, ":", valor)


# 11. FOR COM ENUMERATE()
# FOR WITH ENUMERATE()

# enumerate() retorna o índice e o elemento.
# enumerate() returns the index and the element.

frutas = ["Maçã", "Banana", "Uva"]

for indice, fruta in enumerate(frutas):
    print(indice, fruta)


# 12. ENUMERATE COM INÍCIO PERSONALIZADO
# ENUMERATE WITH CUSTOM START

nomes = ["Ana", "Carlos", "Pedro"]

for indice, nome in enumerate(nomes, start=1):
    print(indice, "-", nome)


# 13. FOR COM IF E ELSE
# FOR WITH IF AND ELSE

numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:
    if numero % 2 == 0:
        print(numero, "é par / is even")
    else:
        print(numero, "é ímpar / is odd")


# 14. FOR COM BREAK
# BREAK STOPS THE LOOP

for numero in range(1, 11):
    if numero == 5:
        break

    print(numero)

# A repetição para quando o número chega a 5.
# The loop stops when the number reaches 5.


# 15. FOR COM CONTINUE
# CONTINUE SKIPS AN ITERATION

for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)

# O número 3 não será exibido.
# Number 3 will not be displayed.


# 16. FOR COM ELSE
# FOR WITH ELSE

for numero in range(1, 4):
    print(numero)
else:
    print("Loop concluído / Loop completed")


# 17. FOR DENTRO DE FOR
# NESTED FOR LOOPS

# Um for dentro de outro for.
# A for loop inside another for loop.

for linha in range(1, 4):
    for coluna in range(1, 4):
        print("Linha:", linha, "| Coluna:", coluna)


# 18. TABUADA COM FOR
# MULTIPLICATION TABLE WITH FOR

numero = 5

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")


# 19. SOMA COM FOR
# SUM WITH FOR

soma = 0

for numero in range(1, 11):
    soma += numero

print("Soma total:", soma)


# 20. FOR COM LIST COMPREHENSION
# FOR WITH LIST COMPREHENSION

# Cria uma lista com os números de 1 até 5.
# Creates a list with numbers from 1 to 5.

numeros = [numero for numero in range(1, 6)]

print(numeros)

# Criando uma lista apenas com números pares.
# Creating a list with only even numbers.

pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print(pares)


# 21. FOR COM ZIP()
# FOR WITH ZIP()

# Percorre duas listas simultaneamente.
# Iterates through two lists simultaneously.

nomes = ["Ana", "Carlos", "Pedro"]
idades = [20, 25, 30]

for nome, idade in zip(nomes, idades):
    print(nome, "-", idade, "anos")


# 22. FOR COM SUM(), MAX() E MIN()
# FOR WITH SUM(), MAX() AND MIN()

numeros = [10, 20, 30, 40, 50]

print("Soma:", sum(numeros))
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))


# 23. FOR COM INPUT()
# FOR WITH USER INPUT

# Solicita cinco nomes ao usuário.
# Requests five names from the user.

nomes = []

for contador in range(5):
    nome = input("Digite um nome / Enter a name: ")
    nomes.append(nome)

print("Nomes cadastrados / Registered names:", nomes)


# 24. FOR PARA CONTAR ELEMENTOS
# FOR TO COUNT ELEMENTS

frutas = ["Maçã", "Banana", "Uva", "Maçã"]

contador = 0

for fruta in frutas:
    if fruta == "Maçã":
        contador += 1

print("Quantidade de maçãs:", contador)


# ============================================================
# 25. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Exiba os números de 1 até 10.
# Display numbers from 1 to 10.

for numero in range(1, 11):
    print(numero)


# EXERCÍCIO 2 / EXERCISE 2
# Exiba apenas os números pares de 1 até 20.
# Display only even numbers from 1 to 20.

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)


# EXERCÍCIO 3 / EXERCISE 3
# Calcule a soma dos números de 1 até 100.
# Calculate the sum of numbers from 1 to 100.

soma = 0

for numero in range(1, 101):
    soma += numero

print("Soma:", soma)


# EXERCÍCIO 4 / EXERCISE 4
# Percorra uma lista e exiba seus elementos.
# Iterate through a list and display its elements.

frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)


# EXERCÍCIO 5 / EXERCISE 5
# Crie a tabuada de um número.
# Create the multiplication table of a number.

numero = 7

for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")


# EXERCÍCIO 6 / EXERCISE 6
# Conte quantas vogais existem em uma palavra.
# Count how many vowels exist in a word.

palavra = "Programacao"
vogais = "aeiou"
contador = 0

for letra in palavra.lower():
    if letra in vogais:
        contador += 1

print("Quantidade de vogais:", contador)


# ============================================================
# 26. EXERCÍCIOS PARA PRATICAR / PRACTICE EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Utilize for para exibir os números de 1 até 50.
# Use for to display numbers from 1 to 50.


# EXERCÍCIO 2 / EXERCISE 2
# Exiba somente os números ímpares de 1 até 30.
# Display only odd numbers from 1 to 30.


# EXERCÍCIO 3 / EXERCISE 3
# Crie uma lista com cinco frutas e percorra utilizando for.
# Create a list with five fruits and iterate using for.


# EXERCÍCIO 4 / EXERCISE 4
# Solicite cinco números ao usuário e calcule a soma.
# Request five numbers from the user and calculate the sum.


# EXERCÍCIO 5 / EXERCISE 5
# Crie uma tabuada de um número informado pelo usuário.
# Create a multiplication table for a number entered by the user.


# EXERCÍCIO 6 / EXERCISE 6
# Percorra uma palavra e conte quantas letras ela possui.
# Iterate through a word and count how many letters it has.


# ============================================================
# 27. RESUMO / SUMMARY
# ============================================================

# for        = percorre uma sequência / iterates through a sequence
# range()    = gera uma sequência numérica / generates a number sequence
# break      = interrompe o loop / stops the loop
# continue   = pula uma repetição / skips an iteration
# enumerate  = retorna índice e elemento / returns index and element
# zip()      = percorre sequências juntas / iterates through sequences together
# append()   = adiciona elemento à lista / adds an element to a list
# sum()      = calcula a soma / calculates the sum
# max()      = retorna o maior valor / returns the maximum value
# min()      = retorna o menor valor / returns the minimum value

# IMPORTANTE / IMPORTANT:
# range(5)       = 0, 1, 2, 3, 4
# range(1, 5)    = 1, 2, 3, 4
# range(1, 10, 2)= 1, 3, 5, 7, 9
#
# O último valor do range não é incluído.
# The last value of range is not included.

# ============================================================
# FIM DO MATERIAL / END OF MATERIAL
# ============================================================
