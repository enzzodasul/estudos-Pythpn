# ============================================================
# OPERADORES LÓGICOS EM PYTHON
# LOGICAL OPERATORS IN PYTHON
# ============================================================

# 1. AND (E)
# Retorna True quando TODAS as condições são verdadeiras.
# Returns True when ALL conditions are true.

idade = 20
tem_carteira = True

print("AND:", idade >= 18 and tem_carteira)
# Resultado / Result: True


# ============================================================
# 2. OR (OU)
# Retorna True quando PELO MENOS UMA condição é verdadeira.
# Returns True when AT LEAST ONE condition is true.

tem_ingresso = False
nome_na_lista = True

print("OR:", tem_ingresso or nome_na_lista)
# Resultado / Result: True


# ============================================================
# 3. NOT (NÃO)
# Inverte o valor lógico: True vira False e False vira True.
# Reverses the logical value: True becomes False and False becomes True.

esta_chovendo = False

print("NOT:", not esta_chovendo)
# Resultado / Result: True


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# and -> E: todas as condições precisam ser verdadeiras.
# and -> AND: all conditions must be true.

# or  -> OU: pelo menos uma condição precisa ser verdadeira.
# or  -> OR: at least one condition must be true.

# not -> NÃO: inverte o valor lógico.
# not -> NOT: reverses the logical value.
