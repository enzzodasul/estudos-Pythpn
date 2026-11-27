#Exercício 1: Cálculo de Juros Compostos Crie um programa que calcule o montante final de um investimento com juros compostos. O programa deve solicitar ao usuário o valor principal, a taxa de juros anual e o número de anos de investimento. Em seguida, ele deve calcular e exibir o montante total.

#solicited user dates

principal_amount = float(input("enter the initial investment amount: R$ "))
interest_rate = float(input("enter the interest rate annually (%): "))
years = int(input("enter the number of years: "))

#converte a taxa percetual para decimal
rate = interest_rate / 100

#calcula o montante com juros compostos
amount = principal_amount * (1 + rate) ** years

#exibe o resultado
print(f"\nthe final amount will be: {amount:.2f}")



#-----------------------------------------------------------------------------------------


#Exercício 2: Conversão de Unidades Crie um programa que converta uma medida em metros para centímetros e milímetros. O usuário deve inserir o valor em metros, e o programa deve calcular e exibir as correspondentes medidas em centímetros e milímetros.



# Exercício 2: Conversão de Unidades

# Solicita uma medida em metros
metros = float(input("Digite a medida em metros: "))

# Realiza as conversões
centimetros = metros * 100
milimetros = metros * 1000

# Exibe os resultados
print(f"\nMedida em metros: {metros:.2f} m")
print(f"Medida em centímetros: {centimetros:.2f} cm")
print(f"Medida em milímetros: {milimetros:.2f} mm")


#-----------------------------------------------------------------------------------------





#Exercício 3: Calculadora de IMC Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar ao usuário o peso em quilogramas e a altura em metros, e em seguida calcular e exibir o IMC.


# Exercício 3: Calculadora de IMC

# Solicita os dados ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"\nSeu IMC é: {imc:.2f}")
