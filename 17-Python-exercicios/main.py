
# ============================================================
# EXERCÍCIO 1: CRIAR UM DICIONÁRIO
# EXERCISE 1: CREATE A DICTIONARY
# ============================================================
#
# Crie um dicionário com informações básicas:
# nome, idade e cidade.
#
# Create a dictionary with basic information:
# name, age and city.
#
# Cada informação possui uma chave e um valor.
# Each piece of information has a key and a value.

pessoa = {
    "nome": "Enzo",
    "idade": 20,
    "cidade": "Juiz de Fora"
}

print("EXERCÍCIO 1 - INFORMAÇÕES PESSOAIS")
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

print("Dicionário completo:", pessoa)


# ============================================================
# EXERCÍCIO 2: ACESSAR VALOR
# EXERCISE 2: ACCESS A VALUE
# ============================================================
#
# Dado um dicionário de cores e seus códigos hexadecimais,
# acesse o código hexadecimal da cor vermelho e exiba-o.
#
# Given a dictionary of colors and their hexadecimal codes,
# access the hexadecimal code for red and display it.
#
# Utilizamos a chave "vermelho" para acessar seu valor.
# We use the key "vermelho" to access its value.

cores = {
    "vermelho": "#FF0000",
    "verde": "#008000",
    "azul": "#0000FF",
    "amarelo": "#FFFF00"
}

codigo_vermelho = cores["vermelho"]

print("\nEXERCÍCIO 2 - CÓDIGO HEXADECIMAL")
print("Código hexadecimal do vermelho:", codigo_vermelho)


# ============================================================
# EXERCÍCIO 3: ADICIONAR E ALTERAR VALORES
# EXERCISE 3: ADD AND MODIFY VALUES
# ============================================================
#
# Crie um dicionário com palavras e suas definições.
# Adicione uma nova palavra e altere a definição
# de uma palavra existente.
#
# Create a dictionary with words and their definitions.
# Add a new word and change the definition
# of an existing word.
#
# ADICIONAR:
# dicionario["nova_chave"] = "novo valor"
#
# MODIFY:
# dictionary["existing_key"] = "new value"

dicionario = {
    "Python": "Linguagem de programação.",
    "Variável": "Espaço utilizado para armazenar dados.",
    "Função": "Bloco de código que executa uma tarefa."
}

# Exibindo o dicionário original.
# Displaying the original dictionary.

print("\nEXERCÍCIO 3 - DICIONÁRIO ORIGINAL")
print(dicionario)

# Adicionando uma nova palavra.
# Adding a new word.

dicionario["Tupla"] = "Coleção ordenada e imutável de elementos."

# Alterando a definição de uma palavra existente.
# Modifying the definition of an existing word.

dicionario["Python"] = "Linguagem de programação de alto nível."

# Exibindo o resultado final.
# Displaying the final result.

print("\nDICIONÁRIO ATUALIZADO")

for palavra, definicao in dicionario.items():
    print(palavra, ":", definicao)


# ============================================================
# RESUMO DOS RESULTADOS
# SUMMARY OF RESULTS
# ============================================================
#
# EXERCÍCIO 1:
# Criamos um dicionário com nome, idade e cidade.
#
# EXERCISE 1:
# We created a dictionary with name, age and city.
#
# EXERCÍCIO 2:
# Acessamos o valor usando cores["vermelho"].
# Resultado: #FF0000
#
# EXERCISE 2:
# We accessed the value using cores["vermelho"].
# Result: #FF0000
#
# EXERCÍCIO 3:
# Adicionamos a palavra "Tupla" e alteramos a definição
# de "Python".
#
# EXERCISE 3:
# We added the word "Tupla" and changed the definition
# of "Python".
#
# ============================================================
