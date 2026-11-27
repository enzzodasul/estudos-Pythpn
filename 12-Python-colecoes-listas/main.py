
# ============================================================
# PYTHON - COLEÇÕES COMPLETAS
# PYTHON - COMPLETE COLLECTIONS
# ============================================================
#
# As coleções permitem armazenar vários valores em uma variável.
# Collections allow you to store multiple values in one variable.
#
# PRINCIPAIS COLEÇÕES / MAIN COLLECTIONS:
#
# 1. LIST  -> Lista       []
# 2. TUPLE -> Tupla       ()
# 3. DICT  -> Dicionário  {}
# 4. SET   -> Conjunto    {}
#
# ============================================================
# 1. LISTAS - LISTS
# ============================================================
#
# Características / Characteristics:
# - São ordenadas / Ordered.
# - Permitem elementos repetidos / Allow duplicates.
# - São modificáveis / Mutable.
# - Aceitam diferentes tipos de dados / Accept different data types.
# - Utilizam colchetes [] / Use square brackets [].
#
# ------------------------------------------------------------
# 1.1 CRIANDO LISTAS / CREATING LISTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva", "Laranja"]
numeros = [10, 20, 30, 40, 50]
misturada = ["Enzo", 20, 1.75, True]
lista_vazia = []

print(frutas)
print(numeros)
print(misturada)
print(lista_vazia)

# ------------------------------------------------------------
# 1.2 ACESSANDO ELEMENTOS / ACCESSING ELEMENTS
# ------------------------------------------------------------
#
# Os índices começam em zero.
# Indexes start at zero.

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

print(frutas[0])   # Maçã
print(frutas[1])   # Banana
print(frutas[2])   # Uva
print(frutas[3])   # Laranja

# Índices negativos / Negative indexes
print(frutas[-1])  # Laranja
print(frutas[-2])  # Uva

# ------------------------------------------------------------
# 1.3 MODIFICANDO ELEMENTOS / MODIFYING ELEMENTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva"]

frutas[0] = "Morango"

print(frutas)

# ------------------------------------------------------------
# 1.4 ADICIONANDO ELEMENTOS / ADDING ELEMENTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana"]

# Adiciona no final / Adds at the end
frutas.append("Uva")

# Adiciona em uma posição / Inserts at a position
frutas.insert(1, "Morango")

# Adiciona vários elementos / Adds multiple elements
frutas.extend(["Abacaxi", "Melancia"])

print(frutas)

# ------------------------------------------------------------
# 1.5 REMOVENDO ELEMENTOS / REMOVING ELEMENTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva", "Laranja"]

# Remove pelo valor / Removes by value
frutas.remove("Banana")

# Remove pelo índice / Removes by index
frutas.pop(0)

# Remove o último elemento / Removes the last element
frutas.pop()

# Limpa toda a lista / Clears the entire list
# frutas.clear()

print(frutas)

# ------------------------------------------------------------
# 1.6 TAMANHO DA LISTA / LIST LENGTH
# ------------------------------------------------------------

numeros = [10, 20, 30, 40, 50]

print(len(numeros))  # 5

# ------------------------------------------------------------
# 1.7 VERIFICANDO ELEMENTOS / CHECKING ELEMENTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva"]

print("Maçã" in frutas)       # True
print("Morango" in frutas)    # False

print("Morango" not in frutas)  # True

# ------------------------------------------------------------
# 1.8 ORGANIZANDO LISTAS / SORTING LISTS
# ------------------------------------------------------------

numeros = [50, 10, 40, 20, 30]

# Ordem crescente / Ascending order
numeros.sort()
print(numeros)

# Ordem decrescente / Descending order
numeros.sort(reverse=True)
print(numeros)

# Inverte a ordem atual / Reverses current order
numeros.reverse()
print(numeros)

# ------------------------------------------------------------
# 1.9 COPIANDO LISTAS / COPYING LISTS
# ------------------------------------------------------------

original = [10, 20, 30]

copia = original.copy()

copia.append(40)

print("Original:", original)
print("Cópia:", copia)

# ------------------------------------------------------------
# 1.10 FATIAMENTO / SLICING
# ------------------------------------------------------------
#
# Sintaxe / Syntax:
# lista[inicio:fim:passo]
# list[start:end:step]
#
# O índice final não é incluído.
# The ending index is not included.

numeros = [10, 20, 30, 40, 50, 60]

print(numeros[0:3])  # [10, 20, 30]
print(numeros[2:5])  # [30, 40, 50]
print(numeros[:3])   # [10, 20, 30]
print(numeros[3:])   # [40, 50, 60]
print(numeros[::2])  # [10, 30, 50]
print(numeros[::-1]) # Lista invertida

# ------------------------------------------------------------
# 1.11 PERCORRENDO LISTAS / LOOPING THROUGH LISTS
# ------------------------------------------------------------

frutas = ["Maçã", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)

# Percorrendo com índice / Looping with index
for indice in range(len(frutas)):
    print(indice, frutas[indice])

# Utilizando enumerate / Using enumerate
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# ------------------------------------------------------------
# 1.12 LIST COMPREHENSION
# ------------------------------------------------------------
#
# Forma compacta de criar listas.
# A compact way to create lists.

quadrados = [numero ** 2 for numero in range(1, 6)]

print(quadrados)  # [1, 4, 9, 16, 25]

pares = [numero for numero in range(1, 11) if numero % 2 == 0]

print(pares)  # [2, 4, 6, 8, 10]


# ============================================================
# 2. TUPLAS - TUPLES
# ============================================================
#
# Características / Characteristics:
# - São ordenadas / Ordered.
# - Permitem elementos repetidos / Allow duplicates.
# - São imutáveis / Immutable.
# - Aceitam diferentes tipos de dados / Accept different data types.
# - Utilizam parênteses () / Use parentheses ().
#
# ------------------------------------------------------------
# 2.1 CRIANDO TUPLAS / CREATING TUPLES
# ------------------------------------------------------------

cores = ("Azul", "Verde", "Vermelho", "Amarelo")

numeros = (10, 20, 30, 40)

misturada = ("Enzo", 20, True)

tupla_vazia = ()

# Tupla com apenas um elemento / Tuple with only one element
unico = (10,)

print(cores)
print(numeros)
print(misturada)
print(unico)

# ------------------------------------------------------------
# 2.2 ACESSANDO ELEMENTOS / ACCESSING ELEMENTS
# ------------------------------------------------------------

cores = ("Azul", "Verde", "Vermelho", "Amarelo")

print(cores[0])
print(cores[1])
print(cores[-1])
print(cores[-2])

# ------------------------------------------------------------
# 2.3 FATIAMENTO / SLICING
# ------------------------------------------------------------

numeros = (10, 20, 30, 40, 50)

print(numeros[0:3])
print(numeros[1:4])
print(numeros[::-1])

# ------------------------------------------------------------
# 2.4 CONTANDO ELEMENTOS / COUNTING ELEMENTS
# ------------------------------------------------------------

numeros = (10, 20, 10, 30, 10, 40)

# Conta quantas vezes aparece / Counts occurrences
print(numeros.count(10))  # 3

# Descobre a posição / Finds the position
print(numeros.index(30))  # 3

# ------------------------------------------------------------
# 2.5 TAMANHO E VERIFICAÇÃO / LENGTH AND CHECKING
# ------------------------------------------------------------

cores = ("Azul", "Verde", "Vermelho")

print(len(cores))
print("Azul" in cores)
print("Preto" not in cores)

# ------------------------------------------------------------
# 2.6 PERCORRENDO TUPLAS / LOOPING THROUGH TUPLES
# ------------------------------------------------------------

cores = ("Azul", "Verde", "Vermelho")

for cor in cores:
    print(cor)

# ------------------------------------------------------------
# 2.7 DESEMPACOTAMENTO / UNPACKING
# ------------------------------------------------------------

pessoa = ("Enzo", 20, "Brasil")

nome, idade, pais = pessoa

print(nome)
print(idade)
print(pais)

# ------------------------------------------------------------
# 2.8 CONVERTENDO LISTA EM TUPLA E VICE-VERSA
# CONVERTING LIST TO TUPLE AND VICE VERSA
# ------------------------------------------------------------

lista = [10, 20, 30]

tupla = tuple(lista)

print(tupla)

nova_lista = list(tupla)

print(nova_lista)

# ATENÇÃO / ATTENTION:
# Não podemos modificar diretamente os elementos de uma tupla.
# We cannot directly modify tuple elements.


# ============================================================
# 3. DICIONÁRIOS - DICTIONARIES
# ============================================================
#
# Características / Characteristics:
# - Armazenam pares de chave e valor / Store key-value pairs.
# - São modificáveis / Mutable.
# - As chaves são únicas / Keys are unique.
# - Preservam a ordem de inserção / Preserve insertion order.
# - Utilizam chaves {} / Use curly braces {}.
#
# ------------------------------------------------------------
# 3.1 CRIANDO DICIONÁRIOS / CREATING DICTIONARIES
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Juiz de Fora",
    "profissao": "Programador"
}

dicionario_vazio = {}

print(pessoa)
print(dicionario_vazio)

# ------------------------------------------------------------
# 3.2 ACESSANDO VALORES / ACCESSING VALUES
# ------------------------------------------------------------

print(pessoa["nome"])
print(pessoa["idade"])

# Utilizando get / Using get
print(pessoa.get("cidade"))

# Se a chave não existir, retorna um valor padrão.
# If the key does not exist, returns a default value.
print(pessoa.get("telefone", "Não cadastrado"))

# ------------------------------------------------------------
# 3.3 ADICIONANDO E MODIFICANDO / ADDING AND MODIFYING
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

# Adicionando / Adding
pessoa["email"] = "enzo@email.com"

# Modificando / Modifying
pessoa["idade"] = 21

# Atualizando várias informações / Updating multiple values
pessoa.update({
    "cidade": "Juiz de Fora",
    "profissao": "Desenvolvedor"
})

print(pessoa)

# ------------------------------------------------------------
# 3.4 REMOVENDO ELEMENTOS / REMOVING ELEMENTS
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

# Remove uma chave e retorna seu valor.
# Removes a key and returns its value.
pessoa.pop("idade")

# Remove o último par inserido.
# Removes the last inserted pair.
pessoa.popitem()

# Limpa o dicionário / Clears the dictionary
# pessoa.clear()

print(pessoa)

# ------------------------------------------------------------
# 3.5 ACESSANDO CHAVES E VALORES / ACCESSING KEYS AND VALUES
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

# Todas as chaves / All keys
print(pessoa.keys())

# Todos os valores / All values
print(pessoa.values())

# Todos os pares / All key-value pairs
print(pessoa.items())

# ------------------------------------------------------------
# 3.6 VERIFICANDO CHAVES / CHECKING KEYS
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

print("nome" in pessoa)       # True
print("telefone" in pessoa)   # False

print("nome" not in pessoa)   # False

# ATENÇÃO / ATTENTION:
# O operador in verifica as chaves, não os valores.
# The in operator checks keys, not values.

# ------------------------------------------------------------
# 3.7 PERCORRENDO DICIONÁRIOS / LOOPING THROUGH DICTIONARIES
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

# Percorrendo as chaves / Looping through keys
for chave in pessoa:
    print(chave)

# Percorrendo os valores / Looping through values
for valor in pessoa.values():
    print(valor)

# Percorrendo chave e valor / Looping through key and value
for chave, valor in pessoa.items():
    print(chave, ":", valor)

# ------------------------------------------------------------
# 3.8 DICIONÁRIOS ANINHADOS / NESTED DICTIONARIES
# ------------------------------------------------------------

alunos = {
    "aluno1": {
        "nome": "Carlos",
        "idade": 20
    },
    "aluno2": {
        "nome": "Maria",
        "idade": 22
    }
}

print(alunos["aluno1"]["nome"])
print(alunos["aluno2"]["idade"])

# ------------------------------------------------------------
# 3.9 DICTIONARY COMPREHENSION
# ------------------------------------------------------------
#
# Forma compacta de criar dicionários.
# A compact way to create dictionaries.

quadrados = {
    numero: numero ** 2
    for numero in range(1, 6)
}

print(quadrados)

# Resultado:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ============================================================
# 4. CONJUNTOS - SETS
# ============================================================
#
# Características / Characteristics:
# - Não permitem elementos duplicados / No duplicate elements.
# - Não possuem índices / No indexes.
# - São modificáveis / Mutable.
# - Não garantem ordem de exibição / No guaranteed display order.
# - Utilizam chaves {} / Use curly braces {}.
#
# ------------------------------------------------------------
# 4.1 CRIANDO CONJUNTOS / CREATING SETS
# ------------------------------------------------------------

numeros = {10, 20, 30, 40, 50}

frutas = {"Maçã", "Banana", "Uva"}

# Elementos repetidos são eliminados.
# Duplicate elements are removed.
valores = {10, 10, 20, 20, 30}

print(numeros)
print(frutas)
print(valores)

# Criando conjunto vazio / Creating an empty set
conjunto_vazio = set()

# ATENÇÃO / ATTENTION:
# {} cria um dicionário vazio, não um conjunto.
# {} creates an empty dictionary, not a set.

# ------------------------------------------------------------
# 4.2 ADICIONANDO ELEMENTOS / ADDING ELEMENTS
# ------------------------------------------------------------

frutas = {"Maçã", "Banana"}

# Adiciona um elemento / Adds one element
frutas.add("Uva")

# Adiciona vários elementos / Adds multiple elements
frutas.update(["Laranja", "Abacaxi"])

print(frutas)

# ------------------------------------------------------------
# 4.3 REMOVENDO ELEMENTOS / REMOVING ELEMENTS
# ------------------------------------------------------------

numeros = {10, 20, 30, 40}

# Remove um elemento; gera erro se não existir.
# Removes an element; raises an error if missing.
numeros.remove(10)

# Remove sem gerar erro se não existir.
# Removes without error if missing.
numeros.discard(50)

# Remove um elemento aleatório / Removes an arbitrary element
# numeros.pop()

# Limpa o conjunto / Clears the set
# numeros.clear()

print(numeros)

# ------------------------------------------------------------
# 4.4 OPERAÇÕES ENTRE CONJUNTOS / SET OPERATIONS
# ------------------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União: elementos de A ou B.
# Union: elements in A or B.
print(A.union(B))
print(A | B)

# Interseção: elementos presentes nos dois.
# Intersection: elements present in both.
print(A.intersection(B))
print(A & B)

# Diferença: elementos de A que não estão em B.
# Difference: elements in A but not in B.
print(A.difference(B))
print(A - B)

# Diferença simétrica: elementos que estão em apenas um.
# Symmetric difference: elements in only one set.
print(A.symmetric_difference(B))
print(A ^ B)

# ------------------------------------------------------------
# 4.5 VERIFICANDO CONJUNTOS / CHECKING SETS
# ------------------------------------------------------------

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# Verifica se um conjunto está contido em outro.
# Checks if a set is contained in another.
print(A.issubset(B))

# Verifica se contém outro conjunto.
# Checks if it contains another set.
print(B.issuperset(A))

# Verifica se não possuem elementos em comum.
# Checks if they have no common elements.
print(A.isdisjoint({7, 8, 9}))


# ============================================================
# 5. COMPARAÇÃO ENTRE AS COLEÇÕES
# COMPARISON BETWEEN COLLECTIONS
# ============================================================
#
# LISTA / LIST:
# [] -> Ordenada, modificável e permite repetidos.
#
# TUPLA / TUPLE:
# () -> Ordenada, imutável e permite repetidos.
#
# DICIONÁRIO / DICTIONARY:
# {} -> Chaves e valores, modificável e chaves únicas.
#
# CONJUNTO / SET:
# {} -> Sem índices, modificável e sem elementos repetidos.
#
# ------------------------------------------------------------
# RESUMO / SUMMARY
# ------------------------------------------------------------
#
# list     -> lista       -> []
# tuple    -> tupla       -> ()
# dict     -> dicionário  -> {"chave": "valor"}
# set      -> conjunto    -> {1, 2, 3}
#
# LISTA: quando precisar adicionar, remover ou modificar dados.
# LIST: when you need to add, remove or modify data.
#
# TUPLA: quando os dados não devem ser alterados.
# TUPLE: when data should not be changed.
#
# DICIONÁRIO: quando precisar relacionar chaves e valores.
# DICTIONARY: when you need key-value relationships.
#
# CONJUNTO: quando precisar evitar valores duplicados.
# SET: when you need to avoid duplicate values.


# ============================================================
# 6. FUNÇÕES ÚTEIS PARA COLEÇÕES
# USEFUL FUNCTIONS FOR COLLECTIONS
# ============================================================

numeros = [10, 20, 30, 40, 50]

print(len(numeros))   # Quantidade / Length
print(max(numeros))   # Maior valor / Maximum
print(min(numeros))   # Menor valor / Minimum
print(sum(numeros))   # Soma / Sum
print(sorted(numeros))  # Lista ordenada / Sorted list

# Conversões / Conversions

lista = [1, 2, 3]
tupla = tuple(lista)
conjunto = set(lista)

print(list(tupla))
print(tuple(conjunto))
print(set(lista))

# Tipos / Types

print(type(lista))
print(type(tupla))
print(type(pessoa))
print(type(conjunto))


# ============================================================
# 7. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ============================================================

# ------------------------------------------------------------
# EXERCÍCIO 1: LISTA DE FRUTAS
# EXERCISE 1: FRUIT LIST
# ------------------------------------------------------------
#
# Crie uma lista com cinco frutas, adicione uma fruta e exiba.
# Create a list with five fruits, add one fruit and display it.

frutas = ["Maçã", "Banana", "Uva", "Pera", "Manga"]

frutas.append("Abacaxi")

print("Frutas:", frutas)

# ------------------------------------------------------------
# EXERCÍCIO 2: SOMA DOS NÚMEROS
# EXERCISE 2: SUM OF NUMBERS
# ------------------------------------------------------------
#
# Crie uma lista de números e calcule a soma.
# Create a list of numbers and calculate the sum.

numeros = [10, 20, 30, 40, 50]

resultado = sum(numeros)

print("Soma:", resultado)

# ------------------------------------------------------------
# EXERCÍCIO 3: TUPLA DE CORES
# EXERCISE 3: COLORS TUPLE
# ------------------------------------------------------------
#
# Crie uma tupla com quatro cores e exiba a primeira.
# Create a tuple with four colors and display the first one.

cores = ("Azul", "Verde", "Vermelho", "Amarelo")

print("Primeira cor:", cores[0])

# ------------------------------------------------------------
# EXERCÍCIO 4: CADASTRO DE PESSOA
# EXERCISE 4: PERSON REGISTRATION
# ------------------------------------------------------------
#
# Crie um dicionário com nome, idade e cidade.
# Create a dictionary with name, age and city.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Juiz de Fora"
}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# ------------------------------------------------------------
# EXERCÍCIO 5: REMOVER DUPLICADOS
# EXERCISE 5: REMOVE DUPLICATES
# ------------------------------------------------------------
#
# Utilize um conjunto para remover valores repetidos.
# Use a set to remove duplicate values.

numeros = [10, 20, 20, 30, 30, 40, 50, 50]

sem_repetidos = set(numeros)

print("Sem repetidos:", sem_repetidos)

# ------------------------------------------------------------
# EXERCÍCIO 6: MÉDIA DE NOTAS
# EXERCISE 6: GRADE AVERAGE
# ------------------------------------------------------------
#
# Calcule a média de três notas armazenadas em uma lista.
# Calculate the average of three grades stored in a list.

notas = [8.0, 7.5, 9.0]

media = sum(notas) / len(notas)

print("Média:", media)

# ------------------------------------------------------------
# EXERCÍCIO 7: ESTOQUE DE PRODUTOS
# EXERCISE 7: PRODUCT INVENTORY
# ------------------------------------------------------------
#
# Crie um dicionário com produtos e quantidades.
# Create a dictionary with products and quantities.

estoque = {
    "Notebook": 10,
    "Mouse": 25,
    "Teclado": 15
}

estoque["Monitor"] = 8

estoque["Mouse"] = 30

print("Estoque:", estoque)

# ------------------------------------------------------------
# EXERCÍCIO 8: UNIÃO DE CONJUNTOS
# EXERCISE 8: SET UNION
# ------------------------------------------------------------
#
# Faça a união de dois conjuntos.
# Perform the union of two sets.

grupo_a = {"Ana", "Carlos", "Maria"}
grupo_b = {"Maria", "João", "Pedro"}

todos = grupo_a.union(grupo_b)

print("Todos os participantes:", todos)


# ============================================================
# 8. EXERCÍCIOS PARA PRATICAR / PRACTICE EXERCISES
# ============================================================
#
# 1. Crie uma lista com 5 números e exiba o maior e o menor.
#    Create a list with 5 numbers and display the maximum and minimum.
#
# 2. Crie uma lista de nomes e remova um nome escolhido.
#    Create a list of names and remove a chosen name.
#
# 3. Crie uma tupla com 5 cidades e exiba a terceira.
#    Create a tuple with 5 cities and display the third one.
#
# 4. Crie um dicionário de um produto com nome, preço e estoque.
#    Create a product dictionary with name, price and stock.
#
# 5. Crie dois conjuntos e mostre a interseção entre eles.
#    Create two sets and display their intersection.
#
# 6. Crie uma lista de notas e calcule a média.
#    Create a list of grades and calculate the average.
#
# 7. Crie um dicionário de alunos e percorra seus dados.
#    Create a student dictionary and loop through its data.
#
# 8. Transforme uma lista com números repetidos em um conjunto.
#    Convert a list with repeated numbers into a set.
#
# ============================================================
# FIM DO CONTEÚDO / END OF CONTENT
# ============================================================
