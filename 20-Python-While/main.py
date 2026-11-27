
# ============================================================
# PYTHON - WHILE
# PYTHON - WHILE LOOPS
# ============================================================

# 1. O QUE É WHILE? / WHAT IS WHILE?
# O while repete um código enquanto a condição for verdadeira.
# While repeats code as long as the condition is true.

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


# 2. SINTAXE DO WHILE / WHILE SYNTAX

# while condição:
#     código que será repetido
#     atualização da variável
#
# while condition:
#     code that will be repeated
#     variable update


# 3. CONTADOR COM WHILE / COUNTER WITH WHILE

contador = 0

while contador < 5:
    print("Contagem:", contador)
    contador += 1


# 4. CONTAGEM REGRESSIVA / COUNTDOWN

numero = 5

while numero > 0:
    print(numero)
    numero -= 1

print("Fim! / Finished!")


# 5. WHILE COM INPUT / WHILE WITH INPUT

resposta = ""

while resposta != "sair":
    resposta = input("Digite algo ou 'sair' para encerrar: ")
    print("Você digitou:", resposta)


# 6. WHILE COM CONDIÇÃO NUMÉRICA
# WHILE WITH A NUMERIC CONDITION

numero = 1

while numero <= 10:
    print(numero)
    numero += 1


# 7. WHILE COM IF E ELSE
# WHILE WITH IF AND ELSE

numero = 1

while numero <= 10:
    if numero % 2 == 0:
        print(numero, "é par / is even")
    else:
        print(numero, "é ímpar / is odd")

    numero += 1


# 8. SOMANDO NÚMEROS COM WHILE
# ADDING NUMBERS WITH WHILE

contador = 1
soma = 0

while contador <= 5:
    soma += contador
    contador += 1

print("Resultado da soma:", soma)


# 9. WHILE COM LISTAS / WHILE WITH LISTS

frutas = ["Maçã", "Banana", "Uva"]

indice = 0

while indice < len(frutas):
    print(frutas[indice])
    indice += 1


# 10. WHILE COM BREAK
# BREAK - INTERROMPE A REPETIÇÃO
# BREAK - STOPS THE LOOP

contador = 1

while contador <= 10:
    print(contador)

    if contador == 5:
        break

    contador += 1


# 11. WHILE COM CONTINUE
# CONTINUE - PULA PARA A PRÓXIMA REPETIÇÃO
# CONTINUE - SKIPS TO THE NEXT ITERATION

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print(contador)


# 12. WHILE COM ELSE
# WHILE WITH ELSE

contador = 1

while contador <= 3:
    print(contador)
    contador += 1
else:
    print("Repetição concluída / Loop completed")


# 13. LOOP INFINITO / INFINITE LOOP

# Um loop infinito acontece quando a condição nunca se torna falsa.
# An infinite loop happens when the condition never becomes false.

# Exemplo:
#
# while True:
#     print("Executando...")
#
# ATENÇÃO: para interromper no terminal, pressione CTRL + C.
# ATTENTION: to stop it in the terminal, press CTRL + C.


# 14. MENU INTERATIVO COM WHILE
# INTERACTIVE MENU WITH WHILE

opcao = ""

while opcao != "3":
    print("\n===== MENU =====")
    print("1 - Olá")
    print("2 - Mostrar mensagem")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! / Hello!")
    elif opcao == "2":
        print("Aprendendo Python! / Learning Python!")
    elif opcao == "3":
        print("Saindo... / Exiting...")
    else:
        print("Opção inválida / Invalid option")


# 15. VALIDAÇÃO DE SENHA COM WHILE
# PASSWORD VALIDATION WITH WHILE

senha = ""

while senha != "python123":
    senha = input("Digite a senha: ")

    if senha != "python123":
        print("Senha incorreta / Incorrect password")

print("Acesso permitido / Access granted")


# 16. TENTATIVAS LIMITADAS / LIMITED ATTEMPTS

senha_correta = "1234"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido / Access granted")
        break
    else:
        tentativas += 1
        print("Senha incorreta / Incorrect password")

else:
    print("Limite de tentativas atingido / Attempt limit reached")


# 17. DIFERENÇA ENTRE WHILE E FOR
# DIFFERENCE BETWEEN WHILE AND FOR

# WHILE:
# Usado quando a repetição depende de uma condição.
# Used when repetition depends on a condition.

contador = 1

while contador <= 3:
    print("While:", contador)
    contador += 1


# FOR:
# Usado frequentemente quando sabemos quantas vezes repetir.
# Often used when we know how many times to repeat.

for numero in range(1, 4):
    print("For:", numero)


# ============================================================
# 18. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Exiba os números de 1 até 10.
# Display numbers from 1 to 10.

contador = 1

while contador <= 10:
    print(contador)
    contador += 1


# EXERCÍCIO 2 / EXERCISE 2
# Exiba os números pares de 1 até 20.
# Display even numbers from 1 to 20.

numero = 1

while numero <= 20:
    if numero % 2 == 0:
        print(numero)

    numero += 1


# EXERCÍCIO 3 / EXERCISE 3
# Calcule a soma dos números de 1 até 100.
# Calculate the sum of numbers from 1 to 100.

numero = 1
soma = 0

while numero <= 100:
    soma += numero
    numero += 1

print("Soma total:", soma)


# EXERCÍCIO 4 / EXERCISE 4
# Solicite números até o usuário digitar zero.
# Request numbers until the user enters zero.

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    print("Você digitou:", numero)
    numero = int(input("Digite outro número (0 para sair): "))

print("Programa encerrado / Program finished")


# EXERCÍCIO 5 / EXERCISE 5
# Conte quantos números positivos foram digitados.
# Count how many positive numbers were entered.
# O programa termina quando o usuário digitar zero.
# The program ends when the user enters zero.

contador_positivos = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    if numero > 0:
        contador_positivos += 1

    numero = int(input("Digite outro número (0 para sair): "))

print("Quantidade de positivos:", contador_positivos)


# ============================================================
# 19. EXERCÍCIOS PARA PRATICAR / PRACTICE EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Utilize while para exibir os números de 1 até 50.
# Use while to display numbers from 1 to 50.


# EXERCÍCIO 2 / EXERCISE 2
# Exiba somente os números ímpares de 1 até 30.
# Display only odd numbers from 1 to 30.


# EXERCÍCIO 3 / EXERCISE 3
# Solicite uma senha até o usuário digitar a senha correta.
# Request a password until the user enters the correct password.


# EXERCÍCIO 4 / EXERCISE 4
# Crie um contador regressivo de 10 até 1.
# Create a countdown from 10 to 1.


# EXERCÍCIO 5 / EXERCISE 5
# Solicite números ao usuário até ele digitar zero.
# Request numbers until the user enters zero.
# Ao final, exiba a soma de todos os números digitados.
# At the end, display the sum of all entered numbers.


# EXERCÍCIO 6 / EXERCISE 6
# Crie um menu com três opções:
# Create a menu with three options:
# 1 - Cadastrar
# 2 - Consultar
# 3 - Sair
# O menu deve continuar aparecendo até o usuário escolher 3.
# The menu must keep appearing until the user chooses 3.


# ============================================================
# 20. RESUMO / SUMMARY
# ============================================================

# while       = repete enquanto a condição for verdadeira
#               repeats while the condition is true

# break       = interrompe o loop
#               stops the loop

# continue    = pula para a próxima repetição
#               skips to the next iteration

# else        = executa quando o while termina normalmente
#               runs when the while loop finishes normally

# += 1        = aumenta o valor em 1
#               increases the value by 1

# -= 1        = diminui o valor em 1
#               decreases the value by 1

# len()       = retorna a quantidade de elementos
#               returns the number of elements

# ATENÇÃO / ATTENTION:
# Sempre atualize a variável utilizada na condição quando necessário.
# Always update the variable used in the condition when necessary.
# Caso contrário, você poderá criar um loop infinito.
# Otherwise, you may create an infinite loop.

# ============================================================
# FIM DO MATERIAL / END OF MATERIAL
# ============================================================
