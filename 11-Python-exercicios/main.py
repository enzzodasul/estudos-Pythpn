# ============================================================
# EXERCÍCIO 1: VERIFICAÇÃO DE NÚMERO NO INTERVALO
# EXERCISE 1: CHECKING IF A NUMBER IS IN A RANGE
# ============================================================

# Solicita um número ao usuário.
# Requests a number from the user.
numero = float(input("Digite um número / Enter a number: "))

# Verifica se o número está entre 10 e 20, inclusive.
# Checks if the number is between 10 and 20, inclusive.
if numero >= 10 and numero <= 20:
    print("O número está no intervalo.")
    print("The number is within the range.")
else:
    print("O número está fora do intervalo.")
    print("The number is outside the range.")


# ============================================================
# EXERCÍCIO 2: VERIFICAÇÃO DE CONDIÇÕES MÚLTIPLAS
# EXERCISE 2: CHECKING MULTIPLE CONDITIONS
# ============================================================

# Solicita a idade e o sexo do usuário.
# Requests the user's age and sex.
idade = int(input("Digite sua idade / Enter your age: "))
sexo = input("Digite seu sexo (M/F) / Enter your sex (M/F): ").upper()

# Verifica se tem pelo menos 18 anos E é do sexo masculino.
# Checks if the user is at least 18 years old AND male.
if idade >= 18 and sexo == "M":
    print("Acesso permitido!")
    print("Access granted!")
else:
    print("Acesso negado!")
    print("Access denied!")


# =========================================================
# EXERCÍCIO 3: VALIDADOR DE SENHA
# EXERCISE 3: PASSWORD VALIDATOR
# ========================================================

# Solicita que o usuário crie uma senha.
# Asks the user to create a password.
senha = input("Crie uma senha / Create a password: ")

# Verifica se existe pelo menos uma letra maiúscula.
# Checks if there is at least one uppercase letter.
tem_maiuscula = any(letra.isupper() for letra in senha)

# Verifica se existe pelo menos um número.
# Checks if there is at least one number.
tem_numero = any(caractere.isdigit() for caractere in senha)

# A senha precisa ter pelo menos 8 caracteres
# E conter uma letra maiúscula OU um número.
# The password must have at least 8 characters
# AND contain an uppercase letter OR a number.
if len(senha) >= 8 and (tem_maiuscula or tem_numero):
    print("Senha válida!")
    print("Valid password!")
else:
    print("Senha inválida!")
    print("Invalid password!")

    print("A senha deve ter pelo menos 8 caracteres.")
    print("The password must have at least 8 characters.")

    print("Também deve conter uma letra maiúscula ou um número.")
    print("It must also contain an uppercase letter or a number.")
