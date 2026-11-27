
# ============================================================
# 1. O QUE É ENCAPSULAMENTO?
# 1. WHAT IS ENCAPSULATION?
# ============================================================

# PT: Encapsulamento controla o acesso aos atributos e métodos
# de uma classe, protegendo os dados contra alterações indevidas.
#
# EN: Encapsulation controls access to a class's attributes and
# methods, protecting data from improper changes.

# Exemplo / Example:
# Uma conta bancária controla como o saldo pode ser alterado.
# A bank account controls how its balance can be changed.


# ============================================================
# 2. TIPOS DE ATRIBUTOS
# 2. TYPES OF ATTRIBUTES
# ============================================================

# PÚBLICO / PUBLIC
# PT: Pode ser acessado e modificado diretamente.
# EN: Can be accessed and modified directly.

class PessoaPublica:

    def __init__(self, nome):
        self.nome = nome


pessoa = PessoaPublica("Enzo")

print(pessoa.nome)

pessoa.nome = "Carlos"

print(pessoa.nome)


# PROTEGIDO / PROTECTED
# PT: Um underline indica uso interno por convenção.
# EN: An underscore indicates internal use by convention.

class PessoaProtegida:

    def __init__(self, nome):
        self._nome = nome


pessoa = PessoaProtegida("Enzo")

print(pessoa._nome)


# PRIVADO / PRIVATE
# PT: Dois underlines ativam o mecanismo name mangling.
# EN: Two underscores activate the name mangling mechanism.

class PessoaPrivada:

    def __init__(self, nome):
        self.__nome = nome

    def consultar_nome(self):
        return self.__nome


pessoa = PessoaPrivada("Enzo")

print(pessoa.consultar_nome())


# ============================================================
# 3. GETTERS
# 3. GETTERS
# ============================================================

# PT: Getter é um método utilizado para consultar um atributo.
# EN: A getter is a method used to retrieve an attribute.

class Pessoa:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade


pessoa = Pessoa("Enzo", 20)

print(pessoa.get_nome())
print(pessoa.get_idade())


# ============================================================
# 4. SETTERS
# 4. SETTERS
# ============================================================

# PT: Setter modifica um atributo permitindo validar o novo valor.
# EN: A setter modifies an attribute while allowing value validation.

class Pessoa:

    def __init__(self, idade):
        self.__idade = idade

    def get_idade(self):
        return self.__idade

    def set_idade(self, nova_idade):

        if nova_idade < 0:
            print("Idade inválida!")
            return

        self.__idade = nova_idade


pessoa = Pessoa(20)

print(pessoa.get_idade())

pessoa.set_idade(21)

print(pessoa.get_idade())

pessoa.set_idade(-5)


# ============================================================
# 5. PROPERTY
# 5. PROPERTY
# ============================================================

# PT: @property permite acessar um método como se fosse atributo.
# EN: @property allows a method to be accessed like an attribute.

class Produto:

    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco


produto = Produto(100)

print(produto.preco)


# ============================================================
# 6. PROPERTY COM SETTER
# 6. PROPERTY WITH SETTER
# ============================================================

# PT: @property.setter permite modificar uma propriedade com validação.
# EN: @property.setter allows a property to be modified with validation.

class Produto:

    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):

        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo!")

        self.__preco = novo_preco


produto = Produto(100)

print(produto.preco)

produto.preco = 150

print(produto.preco)

# PT: O valor negativo gera um erro.
# EN: A negative value raises an error.

# produto.preco = -50


# ============================================================
# 7. ENCAPSULAMENTO NA PRÁTICA — CONTA BANCÁRIA
# 7. PRACTICAL ENCAPSULATION — BANK ACCOUNT
# ============================================================

class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    # Consultar saldo / Check balance
    @property
    def saldo(self):
        return self.__saldo

    # Depositar dinheiro / Deposit money
    def depositar(self, valor):

        if valor <= 0:
            print("Valor de depósito inválido!")
            return

        self.__saldo += valor

        print(f"Depósito realizado: R$ {valor:.2f}")

    # Sacar dinheiro / Withdraw money
    def sacar(self, valor):

        if valor <= 0:
            print("Valor de saque inválido!")
            return

        if valor > self.__saldo:
            print("Saldo insuficiente!")
            return

        self.__saldo -= valor

        print(f"Saque realizado: R$ {valor:.2f}")

    # Mostrar informações / Display information
    def mostrar_dados(self):

        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta = ContaBancaria("Enzo", 1000)

conta.mostrar_dados()

conta.depositar(500)
conta.sacar(200)
conta.sacar(5000)

conta.mostrar_dados()

# Resultado final / Final result:
# Titular: Enzo
# Saldo: R$ 1300.00


# ============================================================
# 8. ENCAPSULAMENTO EM PYTHON E JAVASCRIPT
# 8. ENCAPSULATION IN PYTHON AND JAVASCRIPT
# ============================================================

# PYTHON:
# self.nome       -> Atributo da instância
# self._nome      -> Uso interno por convenção
# self.__nome     -> Name mangling
# @property       -> Getter como propriedade
# @nome.setter    -> Setter como propriedade

# JAVASCRIPT:
# this.nome       -> Atributo da instância
# #nome           -> Campo privado
# get nome()      -> Getter
# set nome(valor) -> Setter

# PT: Python utiliza convenções e name mangling.
# EN: Python uses conventions and name mangling.


# ============================================================
# 9. EXERCÍCIOS RESOLVIDOS
# 9. SOLVED EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Crie uma classe Pessoa com nome privado e getter.
# Create a Person class with a private name and a getter.

class Pessoa:

    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


pessoa = Pessoa("Enzo")

print(pessoa.get_nome())


# EXERCÍCIO 2 / EXERCISE 2
# Crie uma classe Produto com preço privado e validação.
# Create a Product class with a private price and validation.

class Produto:

    def __init__(self, preco):
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):

        if novo_preco < 0:
            raise ValueError("Preço inválido!")

        self.__preco = novo_preco


produto = Produto(100)

produto.preco = 200

print(produto.preco)


# EXERCÍCIO 3 / EXERCISE 3
# Crie uma conta com saldo privado e método de depósito.
# Create an account with a private balance and a deposit method.

class Conta:

    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, valor):

        if valor <= 0:
            print("Depósito inválido!")
            return

        self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo


conta = Conta(500)

conta.depositar(300)

print(conta.consultar_saldo())  # 800


# ============================================================
# 10. EXERCÍCIOS PARA PRATICAR
# 10. PRACTICE EXERCISES
# ============================================================

# 1. Crie uma classe Aluno com nome e nota privados.
#    Create a Student class with private name and grade attributes.

# 2. Crie um getter para consultar a nota.
#    Create a getter to retrieve the grade.

# 3. Crie um setter que aceite notas entre 0 e 10.
#    Create a setter that accepts grades between 0 and 10.

# 4. Crie uma classe ContaBancaria com saldo privado.
#    Create a BankAccount class with a private balance.

# 5. Crie métodos para depositar e sacar dinheiro.
#    Create methods to deposit and withdraw money.

# 6. Crie uma classe Funcionario com salário privado e uma
#    propriedade que impeça valores negativos.
#    Create an Employee class with a private salary and a
#    property that prevents negative values.


# ============================================================
# 11. RESUMO GERAL
# 11. GENERAL SUMMARY
# ============================================================

# Encapsulamento / Encapsulation:
# Controla o acesso aos dados de uma classe.
# Controls access to a class's data.

# Público / Public:
# Acesso direto.
# Direct access.

# Protegido / Protected:
# Uso interno por convenção (_atributo).
# Internal use by convention (_attribute).

# Privado / Private:
# Name mangling (__atributo).
# Name mangling (__attribute).

# Getter:
# Consulta um atributo.
# Retrieves an attribute.

# Setter:
# Modifica um atributo com validações.
# Modifies an attribute with validation.

# @property:
# Permite acessar um método como atributo.
# Allows a method to be accessed like an attribute.
