
# ============================================================
# EXERCÍCIOS DE ENCAPSULAMENTO / ENCAPSULATION EXERCISES
# ============================================================

# ------------------------------------------------------------
# EXERCÍCIO 1: CLASSE DE CONTA BANCÁRIA ENCAPSULADA
# EXERCISE 1: ENCAPSULATED BANK ACCOUNT CLASS
# ------------------------------------------------------------

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado / Private attribute

    def depositar(self, valor):
        # Verifica se o valor é positivo / Checks if the amount is positive
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        # Verifica o saldo disponível / Checks available balance
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado!")
        else:
            print("Saldo insuficiente!")

    def consultar_saldo(self):
        # Retorna o saldo / Returns the balance
        return self.__saldo


# Teste / Test
conta = ContaBancaria("Enzzo", 1000)

conta.depositar(500)
conta.sacar(200)

print(f"Titular: {conta.titular}")
print(f"Saldo atual: R$ {conta.consultar_saldo():.2f}")

# Resultado esperado / Expected output:
# Depósito de R$ 500.00 realizado!
# Saque de R$ 200.00 realizado!
# Titular: Enzzo
# Saldo atual: R$ 1300.00


# ------------------------------------------------------------
# EXERCÍCIO 2: CLASSE DE PRODUTO ENCAPSULADA
# EXERCISE 2: ENCAPSULATED PRODUCT CLASS
# ------------------------------------------------------------

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Métodos para consultar os atributos / Methods to access attributes
    def consultar_nome(self):
        return self.__nome

    def consultar_preco(self):
        return self.__preco

    def consultar_quantidade(self):
        return self.__quantidade

    # Métodos para modificar os atributos / Methods to modify attributes
    def alterar_nome(self, novo_nome):
        if novo_nome:
            self.__nome = novo_nome

    def alterar_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("O preço deve ser positivo.")

    def alterar_quantidade(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("A quantidade não pode ser negativa.")

    def exibir_informacoes(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Quantidade: {self.__quantidade}")


# Teste / Test
produto = Produto("Notebook", 3500, 10)

produto.alterar_preco(3200)
produto.alterar_quantidade(15)

produto.exibir_informacoes()

# Resultado esperado / Expected output:
# Produto: Notebook
# Preço: R$ 3200.00
# Quantidade: 15


# ------------------------------------------------------------
# EXERCÍCIO 3: CLASSE DE PESSOA ENCAPSULADA COM MÉTODOS
# EXERCISE 3: ENCAPSULATED PERSON CLASS WITH METHODS
# ------------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    # Método para alterar o email / Method to change the email
    def alterar_email(self, novo_email):
        if "@" in novo_email:
            self.__email = novo_email
            print("Email atualizado com sucesso!")
        else:
            print("Email inválido!")

    # Método para exibir as informações / Method to display information
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")
        print(f"Email: {self.__email}")


# Teste / Test
pessoa = Pessoa("Enzzo", 22, "enzzo@email.com")

pessoa.alterar_email("novo@email.com")
pessoa.exibir_informacoes()

# Resultado esperado / Expected output:
# Email atualizado com sucesso!
# Nome: Enzzo
# Idade: 22
# Email: novo@email.com


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# __atributo:
# Atributo privado / Private attribute.
# Evita acesso direto acidental ao atributo.
# Helps prevent accidental direct access to the attribute.

# Métodos públicos:
# Permitem consultar ou modificar atributos privados.
# Allow accessing or modifying private attributes.

# Encapsulamento:
# Protege os dados e controla como eles são utilizados.
# Protects data and controls how it is used.

# IMPORTANTE / IMPORTANT:
# Em Python, __atributo utiliza name mangling.
# Não é privacidade absoluta, mas dificulta o acesso acidental.
# In Python, __attribute uses name mangling.
# It is not absolute privacy, but helps prevent accidental access.
