
# ============================================================
# EXERCÍCIO 1: CÁLCULO DO PERÍMETRO E ÁREA DO RETÂNGULO
# EXERCISE 1: RECTANGLE PERIMETER AND AREA CALCULATION
# ============================================================

# QUESTÃO / QUESTION:
# Solicite a largura e a altura de um retângulo.
# Ask the user for the width and height of a rectangle.
# Calcule e exiba sua área e seu perímetro.
# Calculate and display its area and perimeter.

# RESPOSTA / ANSWER:

# Solicita os valores ao usuário / Requests values from the user
largura = float(input("Digite a largura / Enter the width: "))
altura = float(input("Digite a altura / Enter the height: "))

# Calcula a área / Calculates the area
area = largura * altura

# Calcula o perímetro / Calculates the perimeter
perimetro = 2 * (largura + altura)

# Exibe os resultados / Displays the results
print("\nÁrea / Area:", area)
print("Perímetro / Perimeter:", perimetro)


# ============================================================
# EXERCÍCIO 2: CONVERSÃO DE MOEDA
# EXERCISE 2: CURRENCY CONVERSION
# ============================================================

# QUESTÃO / QUESTION:
# Converta uma quantia em dólares para euros usando
# uma taxa de câmbio fixa.
# Convert an amount in dollars to euros using
# a fixed exchange rate.

# RESPOSTA / ANSWER:

# Define a taxa de câmbio / Defines the exchange rate
taxa_cambio = 0.92

# Solicita o valor em dólares / Requests the amount in dollars
dolares = float(input("Digite o valor em dólares / Enter the amount in dollars: "))

# Converte dólares para euros / Converts dollars to euros
euros = dolares * taxa_cambio

# Exibe os resultados / Displays the results
print(f"\nDólares / Dollars: $ {dolares:.2f}")
print(f"Euros / Euros: € {euros:.2f}")


# ============================================================
# EXERCÍCIO 3: CALCULADORA DE DESCONTO
# EXERCISE 3: DISCOUNT CALCULATOR
# ============================================================

# QUESTÃO / QUESTION:
# Solicite o preço original de um produto e o percentual
# de desconto. Calcule o desconto e o preço final.
# Ask for the original product price and discount percentage.
# Calculate the discount and the final price.

# RESPOSTA / ANSWER:

# Solicita o preço original / Requests the original price
preco = float(input("Digite o preço / Enter the price: R$ "))

# Solicita o percentual de desconto / Requests the discount percentage
desconto = float(input("Digite o desconto / Enter the discount (%): "))

# Calcula o valor do desconto / Calculates the discount amount
valor_desconto = preco * (desconto / 100)

# Calcula o preço final / Calculates the final price
preco_final = preco - valor_desconto

# Exibe os resultados / Displays the results
print(f"\nPreço original / Original price: R$ {preco:.2f}")
print(f"Desconto / Discount: R$ {valor_desconto:.2f}")
print(f"Preço final / Final price: R$ {preco_final:.2f}")


# ============================================================
# FIM DOS EXERCÍCIOS / END OF EXERCISES
# ============================================================
