# ============================================================
# EXERCÍCIO 1: LISTA COM TODOS OS DIAS DA SEMANA
# EXERCISE 1: LIST WITH ALL DAYS OF THE WEEK
# ============================================================

# Criando uma lista com os dias da semana.
# Creating a list with the days of the week.

dias_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

print("Dias da semana:", dias_semana)


# ============================================================
# EXERCÍCIO 2: REMOVER O ÚLTIMO ELEMENTO
# EXERCISE 2: REMOVE THE LAST ELEMENT
# ============================================================

# Remove o último elemento da lista usando pop().
# Removes the last element from the list using pop().

dias_semana.pop()

# Mostra a lista atualizada.
# Displays the updated list.

print("Lista após remover:", dias_semana)

# Mostra o tamanho da lista usando len().
# Displays the list length using len().

print("Tamanho da lista:", len(dias_semana))


# ============================================================
# EXERCÍCIO 3: ADICIONAR O ELEMENTO NOVAMENTE
# EXERCISE 3: ADD THE ELEMENT AGAIN
# ============================================================

# Adiciona Domingo novamente usando append().
# Adds Sunday again using append().

dias_semana.append("Domingo")

# Mostra a lista atualizada.
# Displays the updated list.

print("Lista após adicionar:", dias_semana)

# Mostra o tamanho atualizado da lista.
# Displays the updated list length.

print("Tamanho da lista:", len(dias_semana))


# ============================================================
# RESULTADOS ESPERADOS / EXPECTED RESULTS
# ============================================================

# Exercício 1: 7 elementos / 7 elements
# Exercício 2: 6 elementos / 6 elements
# Exercício 3: 7 elementos / 7 elements
