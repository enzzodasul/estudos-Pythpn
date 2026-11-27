
# ============================================================
#                    APOSTILA DE PYTHON
#                     TUPLAS - TUPLES
# ============================================================
#
# CONTEÚDO / CONTENT:
#
# 01. Introdução às tuplas
# 02. Características das tuplas
# 03. Criando tuplas
# 04. Tuplas com um elemento
# 05. Acessando elementos
# 06. Índices positivos e negativos
# 07. Tamanho das tuplas
# 08. Verificando elementos
# 09. Fatiamento (Slicing)
# 10. Imutabilidade
# 11. Métodos count() e index()
# 12. Percorrendo tuplas com for
# 13. Percorrendo tuplas com while
# 14. Desempacotamento (Unpacking)
# 15. Operador * no desempacotamento
# 16. Concatenação
# 17. Repetição
# 18. Comparação de tuplas
# 19. Tuplas aninhadas
# 20. Conversão de tipos
# 21. Funções úteis
# 22. Tuplas com dados de diferentes tipos
# 23. Tuplas como retorno de funções
# 24. Tuplas como chaves de dicionários
# 25. Exemplos práticos
# 26. Exercícios resolvidos
# 27. Exercícios para praticar
# 28. Resumo geral
#
# ============================================================
# 01. INTRODUÇÃO ÀS TUPLAS
# INTRODUCTION TO TUPLES
# ============================================================
#
# Uma tupla é uma coleção que permite armazenar vários valores
# dentro de uma única variável.
#
# A tuple is a collection that allows you to store multiple
# values inside a single variable.
#
# Exemplo / Example:
#
# frutas = ("Maçã", "Banana", "Uva")
#
# As tuplas são utilizadas quando queremos armazenar dados
# que não devem ser modificados diretamente.
#
# Tuples are used when we want to store data that should not
# be directly modified.
#
# ============================================================
# 02. CARACTERÍSTICAS DAS TUPLAS
# TUPLE CHARACTERISTICS
# ============================================================
#
# 1. São ordenadas / Ordered.
# 2. Permitem elementos repetidos / Allow duplicates.
# 3. São imutáveis / Immutable.
# 4. Aceitam diferentes tipos de dados / Accept different types.
# 5. Permitem acesso por índices / Allow index access.
# 6. Utilizam parênteses / Use parentheses.
#
# Exemplo / Example:

frutas = ("Maçã", "Banana", "Uva", "Maçã")

print(frutas)

# Resultado / Result:
# ('Maçã', 'Banana', 'Uva', 'Maçã')


# ============================================================
# 03. CRIANDO TUPLAS
# CREATING TUPLES
# ============================================================
#
# Sintaxe / Syntax:
#
# nome_da_tupla = (elemento1, elemento2, elemento3)
#
# Exemplo / Example:

frutas = ("Maçã", "Banana", "Uva")

numeros = (10, 20, 30, 40, 50)

nomes = ("Carlos", "Maria", "João")

print(frutas)
print(numeros)
print(nomes)

# Tupla com diferentes tipos de dados.
# Tuple with different data types.

pessoa = ("Enzo", 20, 1.75, True)

print(pessoa)

# Tupla vazia / Empty tuple.

tupla_vazia = ()

print(tupla_vazia)


# ============================================================
# 04. TUPLA COM APENAS UM ELEMENTO
# TUPLE WITH ONLY ONE ELEMENT
# ============================================================
#
# Para criar uma tupla com um único elemento, precisamos
# utilizar uma vírgula.
#
# To create a tuple with only one element, we need a comma.

tupla_correta = (10,)

nao_e_tupla = (10)

print(type(tupla_correta))
print(type(nao_e_tupla))

# Resultado:
# <class 'tuple'>
# <class 'int'>


# ============================================================
# 05. ACESSANDO ELEMENTOS
# ACCESSING ELEMENTS
# ============================================================
#
# Os elementos são acessados utilizando índices.
# Elements are accessed using indexes.
#
# O primeiro índice é sempre zero.
# The first index is always zero.

frutas = ("Maçã", "Banana", "Uva", "Laranja")

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

# Resultado:
# Maçã
# Banana
# Uva
# Laranja


# ============================================================
# 06. ÍNDICES POSITIVOS E NEGATIVOS
# POSITIVE AND NEGATIVE INDEXES
# ============================================================
#
# Índices positivos começam em zero.
# Positive indexes start at zero.
#
# Índices negativos começam pelo último elemento.
# Negative indexes start from the last element.

frutas = ("Maçã", "Banana", "Uva", "Laranja")

# Índices positivos / Positive indexes.

print(frutas[0])  # Maçã
print(frutas[1])  # Banana
print(frutas[2])  # Uva

# Índices negativos / Negative indexes.

print(frutas[-1])  # Laranja
print(frutas[-2])  # Uva
print(frutas[-3])  # Banana


# ============================================================
# 07. TAMANHO DAS TUPLAS
# TUPLE LENGTH
# ============================================================
#
# A função len() retorna a quantidade de elementos.
# The len() function returns the number of elements.

frutas = ("Maçã", "Banana", "Uva", "Laranja")

quantidade = len(frutas)

print("Quantidade:", quantidade)

# Resultado / Result: 4


# ============================================================
# 08. VERIFICANDO ELEMENTOS
# CHECKING ELEMENTS
# ============================================================
#
# in verifica se um elemento existe.
# in checks whether an element exists.
#
# not in verifica se um elemento não existe.
# not in checks whether an element does not exist.

frutas = ("Maçã", "Banana", "Uva")

print("Maçã" in frutas)
print("Morango" in frutas)

print("Morango" not in frutas)

# Resultados:
# True
# False
# True


# ============================================================
# 09. FATIAMENTO - SLICING
# ============================================================
#
# O slicing permite acessar uma parte da tupla.
# Slicing allows you to access part of a tuple.
#
# Sintaxe / Syntax:
#
# tupla[inicio:fim:passo]
# tuple[start:end:step]
#
# O índice final não é incluído.
# The ending index is not included.

numeros = (10, 20, 30, 40, 50, 60)

# Primeiros três elementos / First three elements.
print(numeros[0:3])

# Elementos da posição 2 até 4.
# Elements from position 2 to 4.
print(numeros[2:5])

# Do início até a posição 2.
# From the beginning to position 2.
print(numeros[:3])

# Da posição 3 até o final.
# From position 3 to the end.
print(numeros[3:])

# Pulando de dois em dois.
# Skipping every second element.
print(numeros[::2])

# Invertendo a tupla.
# Reversing the tuple.
print(numeros[::-1])


# ============================================================
# 10. IMUTABILIDADE
# IMMUTABILITY
# ============================================================
#
# Tuplas não permitem modificar, adicionar ou remover
# elementos diretamente depois de criadas.
#
# Tuples do not allow directly modifying, adding or removing
# elements after they are created.
#
# Exemplo de operações inválidas:
# Examples of invalid operations:

frutas = ("Maçã", "Banana", "Uva")

# frutas[0] = "Morango"
# ERRO: não podemos modificar uma tupla.
# ERROR: we cannot modify a tuple.

# frutas.append("Laranja")
# ERRO: tuplas não possuem append().
# ERROR: tuples do not have append().

# frutas.remove("Banana")
# ERRO: tuplas não possuem remove().
# ERROR: tuples do not have remove().

# ATENÇÃO:
# Os elementos da tupla não podem ser substituídos.
# ATTENTION:
# Tuple elements cannot be replaced.


# ============================================================
# 11. MÉTODOS COUNT() E INDEX()
# ============================================================
#
# As tuplas possuem dois métodos principais.
# Tuples have two main methods.

numeros = (10, 20, 30, 20, 40, 20, 50)

# COUNT:
# Conta quantas vezes um elemento aparece.
# Counts how many times an element appears.

print(numeros.count(20))

# Resultado: 3

# INDEX:
# Retorna a posição da primeira ocorrência.
# Returns the position of the first occurrence.

print(numeros.index(30))

# Resultado: 2


# ============================================================
# 12. PERCORRENDO TUPLAS COM FOR
# LOOPING THROUGH TUPLES WITH FOR
# ============================================================
#
# O for permite percorrer todos os elementos.
# The for loop allows you to iterate through all elements.

frutas = ("Maçã", "Banana", "Uva")

for fruta in frutas:
    print(fruta)

# Percorrendo com índice.
# Looping with index.

for indice in range(len(frutas)):
    print(indice, frutas[indice])

# Utilizando enumerate().
# Using enumerate().

for indice, fruta in enumerate(frutas):
    print(indice, fruta)


# ============================================================
# 13. PERCORRENDO TUPLAS COM WHILE
# LOOPING THROUGH TUPLES WITH WHILE
# ============================================================

numeros = (10, 20, 30, 40)

indice = 0

while indice < len(numeros):
    print(numeros[indice])

    indice += 1


# ============================================================
# 14. DESEMPACOTAMENTO - UNPACKING
# ============================================================
#
# Permite distribuir os elementos da tupla em variáveis.
# Allows distributing tuple elements into variables.

pessoa = ("Enzo", 20, "Brasil")

nome, idade, pais = pessoa

print(nome)
print(idade)
print(pais)

# Cada variável recebe um elemento correspondente.
# Each variable receives a corresponding element.


# ============================================================
# 15. DESEMPACOTAMENTO COM *
# UNPACKING WITH *
# ============================================================
#
# O operador * captura vários elementos em uma lista.
# The * operator captures multiple elements into a list.

numeros = (10, 20, 30, 40, 50)

primeiro, *meio, ultimo = numeros

print(primeiro)
print(meio)
print(ultimo)

# Resultado:
# 10
# [20, 30, 40]
# 50


# ============================================================
# 16. CONCATENAÇÃO DE TUPLAS
# TUPLE CONCATENATION
# ============================================================
#
# O operador + une duas tuplas.
# The + operator joins two tuples.

tupla1 = (10, 20, 30)

tupla2 = (40, 50, 60)

resultado = tupla1 + tupla2

print(resultado)

# Resultado:
# (10, 20, 30, 40, 50, 60)


# ============================================================
# 17. REPETIÇÃO DE TUPLAS
# TUPLE REPETITION
# ============================================================
#
# O operador * repete os elementos da tupla.
# The * operator repeats tuple elements.

numeros = (10, 20)

resultado = numeros * 3

print(resultado)

# Resultado:
# (10, 20, 10, 20, 10, 20)


# ============================================================
# 18. COMPARAÇÃO DE TUPLAS
# COMPARING TUPLES
# ============================================================

tupla1 = (10, 20, 30)

tupla2 = (10, 20, 30)

tupla3 = (10, 20, 40)

print(tupla1 == tupla2)  # True

print(tupla1 == tupla3)  # False

print(tupla1 != tupla3)  # True

print(tupla1 < tupla3)   # True

# As comparações seguem a ordem dos elementos.
# Comparisons follow the order of elements.


# ============================================================
# 19. TUPLAS ANINHADAS
# NESTED TUPLES
# ============================================================
#
# Uma tupla pode armazenar outras tuplas.
# A tuple can store other tuples.

alunos = (
    ("Carlos", 20),
    ("Maria", 22),
    ("João", 19)
)

print(alunos[0])
print(alunos[0][0])
print(alunos[1][1])

# Percorrendo os alunos.
# Looping through students.

for nome, idade in alunos:
    print("Nome:", nome)
    print("Idade:", idade)


# ============================================================
# 20. CONVERSÃO DE TIPOS
# TYPE CONVERSION
# ============================================================

# Lista para tupla.
# List to tuple.

lista = [10, 20, 30]

tupla = tuple(lista)

print(tupla)

# Tupla para lista.
# Tuple to list.

tupla = (40, 50, 60)

lista = list(tupla)

print(lista)

# String para tupla.
# String to tuple.

palavra = "Python"

letras = tuple(palavra)

print(letras)

# Resultado:
# ('P', 'y', 't', 'h', 'o', 'n')


# ============================================================
# 21. FUNÇÕES ÚTEIS PARA TUPLAS
# USEFUL FUNCTIONS FOR TUPLES
# ============================================================

numeros = (10, 20, 30, 40, 50)

# len() - Quantidade de elementos / Number of elements.
print(len(numeros))

# max() - Maior valor / Maximum value.
print(max(numeros))

# min() - Menor valor / Minimum value.
print(min(numeros))

# sum() - Soma dos elementos / Sum of elements.
print(sum(numeros))

# sorted() - Retorna uma lista ordenada / Returns a sorted list.
print(sorted(numeros))

# type() - Descobre o tipo / Gets the type.
print(type(numeros))


# ============================================================
# 22. TUPLAS COM DIFERENTES TIPOS DE DADOS
# TUPLES WITH DIFFERENT DATA TYPES
# ============================================================

produto = (
    "Notebook",
    3500.00,
    10,
    True
)

nome = produto[0]
preco = produto[1]
estoque = produto[2]
disponivel = produto[3]

print("Produto:", nome)
print("Preço:", preco)
print("Estoque:", estoque)
print("Disponível:", disponivel)


# ============================================================
# 23. TUPLAS COMO RETORNO DE FUNÇÕES
# TUPLES AS FUNCTION RETURNS
# ============================================================
#
# Uma função pode retornar vários valores.
# A function can return multiple values.
#
# O Python empacota esses valores em uma tupla.
# Python packs these values into a tuple.

def calcular(a, b):

    soma = a + b

    subtracao = a - b

    multiplicacao = a * b

    return soma, subtracao, multiplicacao


resultado = calcular(10, 5)

print(resultado)

# Desempacotando o retorno.
# Unpacking the return value.

soma, subtracao, multiplicacao = calcular(10, 5)

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)


# ============================================================
# 24. TUPLAS COMO CHAVES DE DICIONÁRIOS
# TUPLES AS DICTIONARY KEYS
# ============================================================
#
# Tuplas com elementos imutáveis podem ser utilizadas
# como chaves de dicionários.
#
# Tuples containing immutable elements can be used
# as dictionary keys.

localizacoes = {
    (10, 20): "Casa",
    (30, 40): "Escola",
    (50, 60): "Trabalho"
}

print(localizacoes[(10, 20)])
print(localizacoes[(30, 40)])


# ============================================================
# 25. EXEMPLOS PRÁTICOS
# PRACTICAL EXAMPLES
# ============================================================

# ------------------------------------------------------------
# EXEMPLO 1: CADASTRO DE ALUNO
# EXAMPLE 1: STUDENT REGISTRATION
# ------------------------------------------------------------

aluno = ("Enzo", 20, "Python")

nome, idade, curso = aluno

print("Nome:", nome)
print("Idade:", idade)
print("Curso:", curso)


# ------------------------------------------------------------
# EXEMPLO 2: NOTAS DE UM ALUNO
# EXAMPLE 2: STUDENT GRADES
# ------------------------------------------------------------

notas = (8.0, 7.5, 9.0, 10.0)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)


# ------------------------------------------------------------
# EXEMPLO 3: COORDENADAS
# EXAMPLE 3: COORDINATES
# ------------------------------------------------------------

coordenadas = (10.5, 20.8)

latitude, longitude = coordenadas

print("Latitude:", latitude)
print("Longitude:", longitude)


# ------------------------------------------------------------
# EXEMPLO 4: PRODUTO
# EXAMPLE 4: PRODUCT
# ------------------------------------------------------------

produto = ("Mouse", 80.00, 25)

nome, preco, quantidade = produto

valor_total = preco * quantidade

print("Produto:", nome)
print("Preço:", preco)
print("Quantidade:", quantidade)
print("Valor total do estoque:", valor_total)


# ------------------------------------------------------------
# EXEMPLO 5: DIAS DA SEMANA
# EXAMPLE 5: DAYS OF THE WEEK
# ------------------------------------------------------------

dias = (
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
)

print("Primeiro dia:", dias[0])
print("Último dia:", dias[-1])
print("Quantidade:", len(dias))

for dia in dias:
    print(dia)


# ============================================================
# 26. EXERCÍCIOS RESOLVIDOS
# SOLVED EXERCISES
# ============================================================

# ------------------------------------------------------------
# EXERCÍCIO 1: CRIAR UMA TUPLA COM CINCO NOMES
# EXERCISE 1: CREATE A TUPLE WITH FIVE NAMES
# ------------------------------------------------------------

nomes = ("Ana", "Carlos", "Maria", "João", "Pedro")

print(nomes)


# ------------------------------------------------------------
# EXERCÍCIO 2: MOSTRAR O SEGUNDO E QUARTO ELEMENTO
# EXERCISE 2: DISPLAY THE SECOND AND FOURTH ELEMENTS
# ------------------------------------------------------------

print(nomes[1])
print(nomes[3])


# ------------------------------------------------------------
# EXERCÍCIO 3: CRIAR TUPLA COM DEZ NÚMEROS E SOMAR
# EXERCISE 3: CREATE A TUPLE WITH TEN NUMBERS AND SUM
# ------------------------------------------------------------

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Soma:", sum(numeros))


# ------------------------------------------------------------
# EXERCÍCIO 4: CONTAR QUANTAS VEZES O NÚMERO 5 APARECE
# EXERCISE 4: COUNT HOW MANY TIMES NUMBER 5 APPEARS
# ------------------------------------------------------------

valores = (5, 10, 5, 20, 5, 30)

print("Ocorrências:", valores.count(5))


# ------------------------------------------------------------
# EXERCÍCIO 5: VERIFICAR SE PYTHON EXISTE NA TUPLA
# EXERCISE 5: CHECK IF PYTHON EXISTS IN THE TUPLE
# ------------------------------------------------------------

linguagens = ("Python", "Java", "JavaScript", "C++")

print("Python" in linguagens)


# ------------------------------------------------------------
# EXERCÍCIO 6: INVERTER UMA TUPLA
# EXERCISE 6: REVERSE A TUPLE
# ------------------------------------------------------------

numeros = (1, 2, 3, 4, 5)

invertida = numeros[::-1]

print(invertida)


# ------------------------------------------------------------
# EXERCÍCIO 7: CONVERTER TUPLA EM LISTA E ADICIONAR
# EXERCISE 7: CONVERT TUPLE TO LIST AND ADD AN ELEMENT
# ------------------------------------------------------------

cores = ("Azul", "Verde", "Vermelho")

lista_cores = list(cores)

lista_cores.append("Amarelo")

cores = tuple(lista_cores)

print(cores)


# ------------------------------------------------------------
# EXERCÍCIO 8: DESEMPACOTAR UMA TUPLA
# EXERCISE 8: UNPACK A TUPLE
# ------------------------------------------------------------

pessoa = ("Carlos", 25, "Programador")

nome, idade, profissao = pessoa

print(nome)
print(idade)
print(profissao)


# ------------------------------------------------------------
# EXERCÍCIO 9: CONCATENAR DUAS TUPLAS
# EXERCISE 9: CONCATENATE TWO TUPLES
# ------------------------------------------------------------

tupla1 = (1, 2, 3)

tupla2 = (4, 5, 6)

resultado = tupla1 + tupla2

print(resultado)


# ------------------------------------------------------------
# EXERCÍCIO 10: MAIOR E MENOR VALOR
# EXERCISE 10: MAXIMUM AND MINIMUM VALUE
# ------------------------------------------------------------

notas = (8.5, 7.0, 9.5, 6.0, 10.0)

print("Maior:", max(notas))
print("Menor:", min(notas))


# ============================================================
# 27. EXERCÍCIOS PARA PRATICAR
# PRACTICE EXERCISES
# ============================================================
#
# EXERCÍCIO 1:
# Crie uma tupla com todos os dias da semana.
# Create a tuple with all days of the week.
#
# EXERCÍCIO 2:
# Mostre o primeiro, o terceiro e o último elemento.
# Display the first, third and last elements.
#
# EXERCÍCIO 3:
# Mostre quantos elementos existem na tupla.
# Display how many elements exist in the tuple.
#
# EXERCÍCIO 4:
# Crie uma tupla com cinco números e calcule a soma.
# Create a tuple with five numbers and calculate the sum.
#
# EXERCÍCIO 5:
# Conte quantas vezes o número 10 aparece.
# Count how many times the number 10 appears.
#
# EXERCÍCIO 6:
# Verifique se a palavra Python está em uma tupla.
# Check if the word Python is in a tuple.
#
# EXERCÍCIO 7:
# Inverta uma tupla utilizando slicing.
# Reverse a tuple using slicing.
#
# EXERCÍCIO 8:
# Desempacote uma tupla com nome, idade e profissão.
# Unpack a tuple with name, age and profession.
#
# EXERCÍCIO 9:
# Crie duas tuplas e concatene as duas.
# Create two tuples and concatenate them.
#
# EXERCÍCIO 10:
# Converta uma tupla em lista e adicione um elemento.
# Convert a tuple into a list and add an element.
#
# EXERCÍCIO 11:
# Encontre o maior e o menor valor de uma tupla.
# Find the maximum and minimum value of a tuple.
#
# EXERCÍCIO 12:
# Crie uma tupla de notas e calcule a média.
# Create a tuple of grades and calculate the average.
#
# EXERCÍCIO 13:
# Utilize um for para percorrer uma tupla de frutas.
# Use a for loop to iterate through a fruit tuple.
#
# EXERCÍCIO 14:
# Crie uma tupla aninhada com três alunos.
# Create a nested tuple with three students.
#
# EXERCÍCIO 15:
# Crie uma função que retorne dois valores em uma tupla.
# Create a function that returns two values in a tuple.


# ============================================================
# 28. RESUMO GERAL
# GENERAL SUMMARY
# ============================================================
#
# CRIAÇÃO / CREATION:
# tupla = (10, 20, 30)
#
# TUPLA DE UM ELEMENTO / SINGLE-ELEMENT TUPLE:
# tupla = (10,)
#
# ACESSAR ELEMENTO / ACCESS ELEMENT:
# tupla[0]
#
# ÚLTIMO ELEMENTO / LAST ELEMENT:
# tupla[-1]
#
# TAMANHO / LENGTH:
# len(tupla)
#
# CONTAR OCORRÊNCIAS / COUNT OCCURRENCES:
# tupla.count(10)
#
# ENCONTRAR POSIÇÃO / FIND POSITION:
# tupla.index(20)
#
# VERIFICAR EXISTÊNCIA / CHECK EXISTENCE:
# 10 in tupla
#
# VERIFICAR AUSÊNCIA / CHECK ABSENCE:
# 10 not in tupla
#
# FATIAMENTO / SLICING:
# tupla[0:3]
#
# INVERTER / REVERSE:
# tupla[::-1]
#
# CONCATENAR / CONCATENATE:
# tupla1 + tupla2
#
# REPETIR / REPEAT:
# tupla * 3
#
# DESEMPACOTAR / UNPACK:
# a, b, c = tupla
#
# CONVERTER PARA LISTA / CONVERT TO LIST:
# list(tupla)
#
# CONVERTER PARA TUPLA / CONVERT TO TUPLE:
# tuple(lista)
#
# MAIOR VALOR / MAXIMUM:
# max(tupla)
#
# MENOR VALOR / MINIMUM:
# min(tupla)
#
# SOMA / SUM:
# sum(tupla)
#
# ORDENAR / SORT:
# sorted(tupla)
#
# TIPO / TYPE:
# type(tupla)
#
# ============================================================
# DIFERENÇA ENTRE LISTAS E TUPLAS
# DIFFERENCE BETWEEN LISTS AND TUPLES
# ============================================================
#
# LISTA / LIST:
# lista = [10, 20, 30]
# Pode adicionar, remover e modificar elementos.
# You can add, remove and modify elements.
#
# TUPLA / TUPLE:
# tupla = (10, 20, 30)
# Não permite modificar diretamente os elementos.
# Does not allow directly modifying elements.
#
# LISTA = MUTÁVEL / LIST = MUTABLE
# TUPLA = IMUTÁVEL / TUPLE = IMMUTABLE
#
# ============================================================
#                  FIM DA APOSTILA
#                    END OF GUIDE
# ============================================================
