
# ============================================================
#                  APOSTILA DE PYTHON
#                 DICIONÁRIOS - DICTIONARIES
# ============================================================
#
# CONTEÚDO / CONTENT:
#
# 01. Introdução aos dicionários
# 02. Características dos dicionários
# 03. Criando dicionários
# 04. Dicionário vazio
# 05. Acessando valores
# 06. Acessando valores com get()
# 07. Adicionando elementos
# 08. Modificando elementos
# 09. Removendo elementos
# 10. Verificando se uma chave existe
# 11. Quantidade de elementos
# 12. keys(), values() e items()
# 13. Percorrendo dicionários com for
# 14. Percorrendo chaves e valores
# 15. Atualizando com update()
# 16. Removendo com pop() e popitem()
# 17. Limpando com clear()
# 18. Copiando dicionários
# 19. Dicionários aninhados
# 20. Dicionários com listas
# 21. Dicionários com diferentes tipos
# 22. Desempacotamento e operador **
# 23. Dictionary comprehension
# 24. Operadores de dicionários
# 25. Funções úteis
# 26. Métodos completos
# 27. Exemplos práticos
# 28. Exercícios resolvidos
# 29. Exercícios para praticar
# 30. Resumo geral
#
# ============================================================
# 01. INTRODUÇÃO AOS DICIONÁRIOS
# INTRODUCTION TO DICTIONARIES
# ============================================================
#
# Um dicionário é uma estrutura de dados que armazena
# informações em pares de CHAVE e VALOR.
#
# A dictionary is a data structure that stores information
# in KEY and VALUE pairs.
#
# Sintaxe / Syntax:
#
# dicionario = {
#     "chave": "valor"
# }
#
# Exemplo / Example:

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Juiz de Fora"
}

print(pessoa)

# Resultado:
# {'nome': 'Enzo', 'idade': 20, 'cidade': 'Juiz de Fora'}


# ============================================================
# 02. CARACTERÍSTICAS DOS DICIONÁRIOS
# DICTIONARY CHARACTERISTICS
# ============================================================
#
# 1. Armazenam pares de chave e valor.
#    Store key-value pairs.
#
# 2. São mutáveis.
#    They are mutable.
#
# 3. Mantêm a ordem de inserção.
#    They preserve insertion order.
#
# 4. Não permitem chaves duplicadas.
#    They do not allow duplicate keys.
#
# 5. Os valores podem ser repetidos.
#    Values can be repeated.
#
# 6. As chaves devem ser de tipos imutáveis e hashable.
#    Keys must be immutable and hashable.
#
# 7. Os valores podem ter diferentes tipos.
#    Values can have different types.
#
# Exemplo / Example:

produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 10,
    "disponivel": True
}

print(produto)


# ============================================================
# 03. CRIANDO DICIONÁRIOS
# CREATING DICTIONARIES
# ============================================================
#
# Os dicionários utilizam chaves { }.
# Dictionaries use curly brackets { }.
#
# Cada chave é separada do valor por dois-pontos.
# Each key is separated from its value by a colon.
#
# Os pares são separados por vírgulas.
# Pairs are separated by commas.

aluno = {
    "nome": "Carlos",
    "idade": 22,
    "curso": "Python"
}

print(aluno)


# ============================================================
# 04. DICIONÁRIO VAZIO
# EMPTY DICTIONARY
# ============================================================
#
# Podemos criar um dicionário vazio de duas maneiras.
# We can create an empty dictionary in two ways.

dicionario1 = {}

dicionario2 = dict()

print(dicionario1)
print(dicionario2)

# ATENÇÃO:
# {} cria um dicionário vazio, não um conjunto vazio.
# ATTENTION:
# {} creates an empty dictionary, not an empty set.


# ============================================================
# 05. ACESSANDO VALORES
# ACCESSING VALUES
# ============================================================
#
# Podemos acessar um valor utilizando sua chave.
# We can access a value using its key.
#
# Sintaxe / Syntax:
#
# dicionario["chave"]

pessoa = {
    "nome": "Maria",
    "idade": 25,
    "profissao": "Programadora"
}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["profissao"])

# Resultado:
# Maria
# 25
# Programadora

# ATENÇÃO:
# Se a chave não existir, o acesso com [] gera KeyError.
# ATTENTION:
# If the key does not exist, accessing it with [] raises KeyError.


# ============================================================
# 06. ACESSANDO VALORES COM GET()
# ACCESSING VALUES WITH GET()
# ============================================================
#
# O método get() acessa um valor sem gerar KeyError
# quando a chave não existe.
#
# The get() method accesses a value without raising KeyError
# when the key does not exist.

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

print(pessoa.get("nome"))

# Chave inexistente: retorna None por padrão.
# Missing key: returns None by default.

print(pessoa.get("telefone"))

# Podemos definir um valor padrão.
# We can define a default value.

print(pessoa.get("telefone", "Não informado"))

# Resultado:
# Enzo
# None
# Não informado


# ============================================================
# 07. ADICIONANDO ELEMENTOS
# ADDING ELEMENTS
# ============================================================
#
# Para adicionar, basta criar uma nova chave.
# To add an element, simply create a new key.

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

pessoa["cidade"] = "Juiz de Fora"

pessoa["profissao"] = "Desenvolvedor"

print(pessoa)

# Novos pares de chave e valor foram adicionados.
# New key-value pairs have been added.


# ============================================================
# 08. MODIFICANDO ELEMENTOS
# MODIFYING ELEMENTS
# ============================================================
#
# Se a chave já existir, podemos alterar seu valor.
# If the key already exists, we can change its value.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Rio de Janeiro"
}

pessoa["idade"] = 21

pessoa["cidade"] = "Juiz de Fora"

print(pessoa)


# ============================================================
# 09. REMOVENDO ELEMENTOS
# REMOVING ELEMENTS
# ============================================================
#
# Existem diferentes formas de remover elementos.
# There are different ways to remove elements.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

# del:
# Remove um elemento pela chave.
# Removes an element by key.

del pessoa["cidade"]

print(pessoa)

# pop():
# Remove a chave e retorna seu valor.
# Removes a key and returns its value.

idade_removida = pessoa.pop("idade")

print("Idade removida:", idade_removida)
print(pessoa)


# ============================================================
# 10. VERIFICANDO SE UMA CHAVE EXISTE
# CHECKING IF A KEY EXISTS
# ============================================================
#
# O operador in verifica a existência de uma chave.
# The in operator checks whether a key exists.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

print("nome" in pessoa)

print("telefone" in pessoa)

print("telefone" not in pessoa)

# Resultado:
# True
# False
# True
#
# IMPORTANTE:
# in verifica as CHAVES, não os valores.
# in checks KEYS, not values.


# ============================================================
# 11. QUANTIDADE DE ELEMENTOS
# NUMBER OF ELEMENTS
# ============================================================
#
# len() retorna a quantidade de pares de chave e valor.
# len() returns the number of key-value pairs.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

print(len(pessoa))

# Resultado: 3


# ============================================================
# 12. KEYS(), VALUES() E ITEMS()
# ============================================================
#
# keys() retorna as chaves.
# keys() returns the keys.
#
# values() retorna os valores.
# values() returns the values.
#
# items() retorna os pares de chave e valor.
# items() returns key-value pairs.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

print(pessoa.keys())

print(pessoa.values())

print(pessoa.items())

# Convertendo para listas.
# Converting to lists.

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))


# ============================================================
# 13. PERCORRENDO DICIONÁRIOS COM FOR
# LOOPING THROUGH DICTIONARIES WITH FOR
# ============================================================
#
# O for percorre as chaves por padrão.
# The for loop iterates over keys by default.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

for chave in pessoa:
    print(chave)


# ============================================================
# 14. PERCORRENDO CHAVES E VALORES
# LOOPING THROUGH KEYS AND VALUES
# ============================================================
#
# Utilizamos items() para acessar chave e valor juntos.
# We use items() to access keys and values together.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

for chave, valor in pessoa.items():
    print(chave, ":", valor)

# Percorrendo somente os valores.
# Iterating through values only.

for valor in pessoa.values():
    print(valor)

# Percorrendo somente as chaves.
# Iterating through keys only.

for chave in pessoa.keys():
    print(chave)


# ============================================================
# 15. ATUALIZANDO COM UPDATE()
# UPDATING WITH UPDATE()
# ============================================================
#
# update() adiciona ou modifica vários elementos.
# update() adds or modifies multiple elements.

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

pessoa.update({
    "idade": 21,
    "cidade": "Brasil",
    "profissao": "Programador"
})

print(pessoa)


# ============================================================
# 16. REMOVENDO COM POP() E POPITEM()
# REMOVING WITH POP() AND POPITEM()
# ============================================================

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Brasil"
}

# pop():
# Remove uma chave específica.
# Removes a specific key.

valor = pessoa.pop("idade")

print("Valor removido:", valor)
print(pessoa)

# popitem():
# Remove e retorna o último par inserido.
# Removes and returns the last inserted pair.

removido = pessoa.popitem()

print("Par removido:", removido)
print(pessoa)


# ============================================================
# 17. LIMPANDO UM DICIONÁRIO
# CLEARING A DICTIONARY
# ============================================================
#
# clear() remove todos os elementos.
# clear() removes all elements.

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

pessoa.clear()

print(pessoa)

# Resultado: {}


# ============================================================
# 18. COPIANDO DICIONÁRIOS
# COPYING DICTIONARIES
# ============================================================
#
# copy() cria uma cópia superficial (shallow copy).
# copy() creates a shallow copy.

original = {
    "nome": "Enzo",
    "idade": 20
}

copia = original.copy()

copia["nome"] = "Carlos"

print("Original:", original)
print("Cópia:", copia)

# A alteração na cópia não altera o dicionário original
# neste exemplo, pois os valores são simples.
#
# Changing the copy does not change the original dictionary
# in this example because the values are simple.


# ============================================================
# 19. DICIONÁRIOS ANINHADOS
# NESTED DICTIONARIES
# ============================================================
#
# Um dicionário pode armazenar outros dicionários.
# A dictionary can store other dictionaries.

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

print(alunos)

# Acessando dados internos.
# Accessing nested data.

print(alunos["aluno1"]["nome"])

print(alunos["aluno2"]["idade"])

# Modificando dados internos.
# Modifying nested data.

alunos["aluno1"]["idade"] = 21

print(alunos["aluno1"])


# ============================================================
# 20. DICIONÁRIOS COM LISTAS
# DICTIONARIES WITH LISTS
# ============================================================
#
# Um valor de dicionário pode ser uma lista.
# A dictionary value can be a list.

aluno = {
    "nome": "Enzo",
    "notas": [8.0, 9.0, 7.5, 10.0],
    "materias": ["Python", "Matemática", "Inglês"]
}

print(aluno["nome"])

print(aluno["notas"])

print(aluno["notas"][0])

print(aluno["materias"][1])

# Adicionando uma nota.
# Adding a grade.

aluno["notas"].append(9.5)

print(aluno["notas"])


# ============================================================
# 21. DICIONÁRIOS COM DIFERENTES TIPOS
# DICTIONARIES WITH DIFFERENT DATA TYPES
# ============================================================

dados = {
    "nome": "Enzo",
    "idade": 20,
    "altura": 1.75,
    "estudando": True,
    "linguagens": ["Python", "JavaScript"],
    "endereco": {
        "cidade": "Juiz de Fora",
        "estado": "Minas Gerais"
    }
}

print(dados["nome"])
print(dados["linguagens"])
print(dados["endereco"]["cidade"])


# ============================================================
# 22. DESEMPACOTAMENTO E OPERADOR **
# UNPACKING AND ** OPERATOR
# ============================================================
#
# O operador ** pode desempacotar um dicionário
# em argumentos nomeados de uma função.
#
# The ** operator can unpack a dictionary
# into keyword arguments of a function.

def apresentar(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)


pessoa = {
    "nome": "Enzo",
    "idade": 20
}

apresentar(**pessoa)


# Também podemos unir dicionários com **.
# We can also merge dictionaries using **.

dicionario1 = {"a": 1, "b": 2}

dicionario2 = {"c": 3, "d": 4}

resultado = {**dicionario1, **dicionario2}

print(resultado)

# Se houver chaves repetidas, o último valor prevalece.
# If keys are repeated, the last value takes precedence.


# ============================================================
# 23. DICTIONARY COMPREHENSION
# COMPREENSÃO DE DICIONÁRIOS
# ============================================================
#
# Permite criar dicionários de forma compacta.
# Allows creating dictionaries in a compact way.
#
# Sintaxe / Syntax:
#
# {chave: valor for elemento in iteravel}

# Exemplo 1: números e seus quadrados.
# Example 1: numbers and their squares.

quadrados = {
    numero: numero ** 2
    for numero in range(1, 6)
}

print(quadrados)

# Resultado:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Exemplo 2: com condição.
# Example 2: with a condition.

pares = {
    numero: numero * 2
    for numero in range(1, 11)
    if numero % 2 == 0
}

print(pares)


# ============================================================
# 24. OPERADORES DE DICIONÁRIOS
# DICTIONARY OPERATORS
# ============================================================

pessoa = {
    "nome": "Enzo",
    "idade": 20
}

# in: verifica se uma chave existe.
# Checks if a key exists.

print("nome" in pessoa)

# not in: verifica se uma chave não existe.
# Checks if a key does not exist.

print("telefone" not in pessoa)

# ==: compara se os dicionários são iguais.
# Checks whether dictionaries are equal.

outro = {
    "nome": "Enzo",
    "idade": 20
}

print(pessoa == outro)

# !=: verifica se são diferentes.
# Checks whether they are different.

print(pessoa != outro)

# |: une dicionários (Python 3.9+).
# Merges dictionaries (Python 3.9+).

a = {"x": 1}
b = {"y": 2}

print(a | b)


# ============================================================
# 25. FUNÇÕES ÚTEIS
# USEFUL FUNCTIONS
# ============================================================

dados = {
    "a": 10,
    "b": 20,
    "c": 30
}

# len(): quantidade de pares.
print(len(dados))

# list(): converte as chaves em lista.
print(list(dados))

# type(): verifica o tipo.
print(type(dados))

# sum(): soma os valores numéricos.
print(sum(dados.values()))

# max(): maior chave, neste exemplo.
print(max(dados))

# min(): menor chave, neste exemplo.
print(min(dados))


# ============================================================
# 26. MÉTODOS DOS DICIONÁRIOS
# DICTIONARY METHODS
# ============================================================
#
# clear()      -> Remove todos os elementos.
# copy()       -> Cria uma cópia superficial.
# fromkeys()   -> Cria um dicionário a partir de chaves.
# get()        -> Acessa um valor com segurança.
# items()      -> Retorna pares de chave e valor.
# keys()       -> Retorna as chaves.
# pop()        -> Remove uma chave específica.
# popitem()    -> Remove o último par inserido.
# setdefault() -> Retorna uma chave ou insere valor padrão.
# update()     -> Adiciona ou atualiza elementos.
# values()     -> Retorna os valores.
#
# ------------------------------------------------------------
# EXEMPLO DE FROMKEYS()
# FROMKEYS() EXAMPLE
# ------------------------------------------------------------

chaves = ("nome", "idade", "cidade")

novo = dict.fromkeys(chaves, "Não informado")

print(novo)

# ------------------------------------------------------------
# EXEMPLO DE SETDEFAULT()
# SETDEFAULT() EXAMPLE
# ------------------------------------------------------------

pessoa = {
    "nome": "Enzo"
}

# Se a chave não existir, ela será criada.
# If the key does not exist, it will be created.

pessoa.setdefault("idade", 20)

# Se a chave já existir, seu valor não será alterado.
# If the key already exists, its value will not change.

pessoa.setdefault("nome", "Carlos")

print(pessoa)


# ============================================================
# 27. EXEMPLOS PRÁTICOS
# PRACTICAL EXAMPLES
# ============================================================

# ------------------------------------------------------------
# EXEMPLO 1: CADASTRO DE USUÁRIO
# EXAMPLE 1: USER REGISTRATION
# ------------------------------------------------------------

usuario = {
    "nome": "Enzo",
    "email": "enzo@email.com",
    "idade": 20,
    "ativo": True
}

print("Nome:", usuario["nome"])
print("Email:", usuario["email"])
print("Idade:", usuario["idade"])
print("Ativo:", usuario["ativo"])


# ------------------------------------------------------------
# EXEMPLO 2: CONTROLE DE ESTOQUE
# EXAMPLE 2: INVENTORY MANAGEMENT
# ------------------------------------------------------------

estoque = {
    "Notebook": 10,
    "Mouse": 25,
    "Teclado": 15
}

estoque["Mouse"] -= 2

estoque["Monitor"] = 8

print(estoque)


# ------------------------------------------------------------
# EXEMPLO 3: BOLETIM ESCOLAR
# EXAMPLE 3: SCHOOL REPORT
# ------------------------------------------------------------

boletim = {
    "Matemática": 8.5,
    "Português": 9.0,
    "Inglês": 7.5
}

media = sum(boletim.values()) / len(boletim)

print("Média:", media)

for materia, nota in boletim.items():
    print(materia, ":", nota)


# ------------------------------------------------------------
# EXEMPLO 4: CONTADOR DE PALAVRAS
# EXAMPLE 4: WORD COUNTER
# ------------------------------------------------------------

texto = "python java python javascript python java"

palavras = texto.split()

contador = {}

for palavra in palavras:

    if palavra in contador:
        contador[palavra] += 1

    else:
        contador[palavra] = 1

print(contador)

# Resultado:
# {'python': 3, 'java': 2, 'javascript': 1}


# ------------------------------------------------------------
# EXEMPLO 5: CARRINHO DE COMPRAS
# EXAMPLE 5: SHOPPING CART
# ------------------------------------------------------------

carrinho = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Macarrão": 6.00
}

total = sum(carrinho.values())

print("Produtos:", carrinho)
print("Total da compra:", total)


# ============================================================
# 28. EXERCÍCIOS RESOLVIDOS
# SOLVED EXERCISES
# ============================================================

# ------------------------------------------------------------
# EXERCÍCIO 1: CRIAR UM DICIONÁRIO
# EXERCISE 1: CREATE A DICTIONARY
# ------------------------------------------------------------
#
# Crie um dicionário com nome, idade e cidade.
# Create a dictionary with name, age and city.

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

print(pessoa)


# ------------------------------------------------------------
# EXERCÍCIO 2: ACESSAR UM VALOR
# EXERCISE 2: ACCESS A VALUE
# ------------------------------------------------------------
#
# Acesse e exiba a idade.
# Access and display the age.

print(pessoa["idade"])


# ------------------------------------------------------------
# EXERCÍCIO 3: ADICIONAR UMA CHAVE
# EXERCISE 3: ADD A KEY
# ------------------------------------------------------------
#
# Adicione a profissão.
# Add the profession.

pessoa["profissao"] = "Programadora"

print(pessoa)


# ------------------------------------------------------------
# EXERCÍCIO 4: MODIFICAR UM VALOR
# EXERCISE 4: MODIFY A VALUE
# ------------------------------------------------------------
#
# Modifique a idade.
# Modify the age.

pessoa["idade"] = 26

print(pessoa)


# ------------------------------------------------------------
# EXERCÍCIO 5: REMOVER UMA CHAVE
# EXERCISE 5: REMOVE A KEY
# ------------------------------------------------------------
#
# Remova a cidade.
# Remove the city.

pessoa.pop("cidade")

print(pessoa)


# ------------------------------------------------------------
# EXERCÍCIO 6: VERIFICAR UMA CHAVE
# EXERCISE 6: CHECK A KEY
# ------------------------------------------------------------
#
# Verifique se a chave nome existe.
# Check whether the name key exists.

print("nome" in pessoa)


# ------------------------------------------------------------
# EXERCÍCIO 7: CONTAR ELEMENTOS
# EXERCISE 7: COUNT ELEMENTS
# ------------------------------------------------------------
#
# Mostre a quantidade de elementos.
# Display the number of elements.

print(len(pessoa))


# ------------------------------------------------------------
# EXERCÍCIO 8: PERCORRER UM DICIONÁRIO
# EXERCISE 8: ITERATE THROUGH A DICTIONARY
# ------------------------------------------------------------
#
# Exiba todas as chaves e valores.
# Display all keys and values.

for chave, valor in pessoa.items():
    print(chave, ":", valor)


# ------------------------------------------------------------
# EXERCÍCIO 9: SOMAR VALORES
# EXERCISE 9: SUM VALUES
# ------------------------------------------------------------
#
# Crie um dicionário com três preços e calcule o total.
# Create a dictionary with three prices and calculate the total.

precos = {
    "Arroz": 25.00,
    "Feijão": 8.00,
    "Leite": 5.50
}

total = sum(precos.values())

print("Total:", total)


# ------------------------------------------------------------
# EXERCÍCIO 10: DICIONÁRIO ANINHADO
# EXERCISE 10: NESTED DICTIONARY
# ------------------------------------------------------------
#
# Crie um dicionário com os dados de dois alunos.
# Create a dictionary with data from two students.

alunos = {
    "aluno1": {
        "nome": "Carlos",
        "nota": 8.5
    },

    "aluno2": {
        "nome": "Maria",
        "nota": 9.5
    }
}

print(alunos["aluno1"]["nome"])
print(alunos["aluno2"]["nota"])


# ============================================================
# 29. EXERCÍCIOS PARA PRATICAR
# PRACTICE EXERCISES
# ============================================================
#
# EXERCÍCIO 1:
# Crie um dicionário com nome, idade e profissão.
# Create a dictionary with name, age and profession.
#
# EXERCÍCIO 2:
# Acesse e exiba o nome armazenado no dicionário.
# Access and display the name stored in the dictionary.
#
# EXERCÍCIO 3:
# Adicione uma chave chamada "cidade".
# Add a key called "city".
#
# EXERCÍCIO 4:
# Modifique a idade da pessoa.
# Modify the person's age.
#
# EXERCÍCIO 5:
# Remova a profissão do dicionário.
# Remove the profession from the dictionary.
#
# EXERCÍCIO 6:
# Verifique se a chave "email" existe.
# Check whether the "email" key exists.
#
# EXERCÍCIO 7:
# Mostre a quantidade de elementos.
# Display the number of elements.
#
# EXERCÍCIO 8:
# Percorra o dicionário com for e exiba as chaves.
# Iterate through the dictionary with for and display the keys.
#
# EXERCÍCIO 9:
# Percorra o dicionário com items() e exiba chave e valor.
# Iterate using items() and display keys and values.
#
# EXERCÍCIO 10:
# Crie um dicionário com três produtos e seus preços.
# Create a dictionary with three products and their prices.
#
# EXERCÍCIO 11:
# Calcule a soma de todos os preços.
# Calculate the sum of all prices.
#
# EXERCÍCIO 12:
# Crie um dicionário com uma lista de notas.
# Create a dictionary with a list of grades.
#
# EXERCÍCIO 13:
# Crie um dicionário dentro de outro dicionário.
# Create a dictionary inside another dictionary.
#
# EXERCÍCIO 14:
# Utilize update() para atualizar dois valores.
# Use update() to update two values.
#
# EXERCÍCIO 15:
# Crie um dicionário usando dictionary comprehension.
# Create a dictionary using dictionary comprehension.


# ============================================================
# 30. RESUMO GERAL
# GENERAL SUMMARY
# ============================================================
#
# CRIAR DICIONÁRIO / CREATE DICTIONARY:
# pessoa = {"nome": "Enzo", "idade": 20}
#
# DICIONÁRIO VAZIO / EMPTY DICTIONARY:
# pessoa = {}
#
# ACESSAR VALOR / ACCESS VALUE:
# pessoa["nome"]
#
# ACESSAR COM SEGURANÇA / SAFE ACCESS:
# pessoa.get("nome")
#
# ADICIONAR / ADD:
# pessoa["cidade"] = "Brasil"
#
# MODIFICAR / MODIFY:
# pessoa["idade"] = 21
#
# REMOVER / REMOVE:
# del pessoa["idade"]
#
# REMOVER E RETORNAR VALOR / REMOVE AND RETURN VALUE:
# pessoa.pop("idade")
#
# REMOVER ÚLTIMO PAR / REMOVE LAST PAIR:
# pessoa.popitem()
#
# VERIFICAR CHAVE / CHECK KEY:
# "nome" in pessoa
#
# QUANTIDADE / LENGTH:
# len(pessoa)
#
# CHAVES / KEYS:
# pessoa.keys()
#
# VALORES / VALUES:
# pessoa.values()
#
# PARES / ITEMS:
# pessoa.items()
#
# ATUALIZAR / UPDATE:
# pessoa.update({"idade": 25})
#
# COPIAR / COPY:
# pessoa.copy()
#
# LIMPAR / CLEAR:
# pessoa.clear()
#
# VALOR PADRÃO / DEFAULT VALUE:
# pessoa.setdefault("idade", 20)
#
# PERCORRER / ITERATE:
# for chave, valor in pessoa.items():
#     print(chave, valor)
#
# SOMAR VALORES NUMÉRICOS / SUM NUMERIC VALUES:
# sum(pessoa.values())
#
# UNIR DICIONÁRIOS / MERGE DICTIONARIES:
# resultado = dicionario1 | dicionario2
#
# ============================================================
# DIFERENÇA ENTRE LISTAS, TUPLAS E DICIONÁRIOS
# DIFFERENCE BETWEEN LISTS, TUPLES AND DICTIONARIES
# ============================================================
#
# LISTA / LIST:
# lista = [10, 20, 30]
# Armazena elementos em sequência.
# Stores elements in sequence.
# É mutável.
# It is mutable.
#
# TUPLA / TUPLE:
# tupla = (10, 20, 30)
# Armazena elementos em sequência.
# Stores elements in sequence.
# É imutável.
# It is immutable.
#
# DICIONÁRIO / DICTIONARY:
# dicionario = {"nome": "Enzo", "idade": 20}
# Armazena dados em pares de chave e valor.
# Stores data in key-value pairs.
# É mutável.
# It is mutable.
#
# ============================================================
#                  FIM DA APOSTILA
#                    END OF GUIDE
# ============================================================
