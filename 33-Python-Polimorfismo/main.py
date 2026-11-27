
# ============================================================
# POLIMORFISMO EM ORIENTAÇÃO A OBJETOS
# POLYMORPHISM IN OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================

# ------------------------------------------------------------
# 1. O QUE É POLIMORFISMO? / WHAT IS POLYMORPHISM?
# ------------------------------------------------------------

# Polimorfismo permite que diferentes classes utilizem métodos
# com o mesmo nome, mas com comportamentos diferentes.
#
# Polymorphism allows different classes to use methods
# with the same name but different behaviors.
#
# Exemplo: diferentes animais possuem o método emitir_som(),
# mas cada animal emite um som diferente.
#
# Example: different animals have the emitir_som() method,
# but each animal makes a different sound.


# ------------------------------------------------------------
# 2. POLIMORFISMO COM HERANÇA / POLYMORPHISM WITH INHERITANCE
# ------------------------------------------------------------

class Animal:
    def emitir_som(self):
        print("O animal emite um som.")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


class Gato(Animal):
    def emitir_som(self):
        print("Miau!")


class Vaca(Animal):
    def emitir_som(self):
        print("Muuu!")


# Objetos diferentes utilizando o mesmo método.
# Different objects using the same method.

animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    animal.emitir_som()


# ------------------------------------------------------------
# 3. SOBRESCRITA DE MÉTODOS / METHOD OVERRIDING
# ------------------------------------------------------------

# A classe filha pode substituir o comportamento de um método
# herdado da classe pai.
#
# The child class can replace the behavior of an inherited
# method from the parent class.

class Funcionario:
    def calcular_salario(self):
        return 2000


class Gerente(Funcionario):
    def calcular_salario(self):
        return 5000


class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return 4000


funcionarios = [Gerente(), Desenvolvedor()]

for funcionario in funcionarios:
    print(f"Salário: R$ {funcionario.calcular_salario():.2f}")


# ------------------------------------------------------------
# 4. POLIMORFISMO COM FUNÇÕES / POLYMORPHISM WITH FUNCTIONS
# ------------------------------------------------------------

# Uma função pode receber objetos de classes diferentes,
# desde que eles ofereçam o método utilizado.
#
# A function can receive objects from different classes,
# as long as they provide the method being used.

class Carro:
    def mover(self):
        print("O carro está dirigindo.")


class Aviao:
    def mover(self):
        print("O avião está voando.")


class Barco:
    def mover(self):
        print("O barco está navegando.")


def iniciar_movimento(veiculo):
    veiculo.mover()


iniciar_movimento(Carro())
iniciar_movimento(Aviao())
iniciar_movimento(Barco())


# ------------------------------------------------------------
# 5. POLIMORFISMO COM MÉTODOS ESPECIAIS
# POLYMORPHISM WITH SPECIAL METHODS
# ------------------------------------------------------------

# Diferentes classes podem implementar o mesmo método especial,
# como __str__(), para personalizar a representação em texto.
#
# Different classes can implement the same special method,
# such as __str__(), to customize their text representation.

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Pessoa: {self.nome}"


class Produto:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Produto: {self.nome}"


objetos = [Pessoa("Enzzo"), Produto("Notebook")]

for objeto in objetos:
    print(objeto)


# ------------------------------------------------------------
# 6. DUCK TYPING / TIPAGEM DINÂMICA
# ------------------------------------------------------------

# Em Python, não é obrigatório que as classes tenham uma
# classe pai em comum. O importante é oferecer o método esperado.
#
# In Python, classes do not need to share a parent class.
# What matters is providing the expected method.

class Impressora:
    def executar(self):
        print("Imprimindo documento...")


class Scanner:
    def executar(self):
        print("Digitalizando documento...")


def executar_dispositivo(dispositivo):
    dispositivo.executar()


executar_dispositivo(Impressora())
executar_dispositivo(Scanner())


# ------------------------------------------------------------
# 7. POLIMORFISMO COM ABSTRAÇÃO / POLYMORPHISM WITH ABSTRACTION
# ------------------------------------------------------------

# Classes abstratas definem métodos que devem ser implementados
# pelas classes filhas.
#
# Abstract classes define methods that must be implemented
# by their child classes.

from abc import ABC, abstractmethod


class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


formas = [
    Quadrado(5),
    Retangulo(4, 6)
]

for forma in formas:
    print(f"Área: {forma.calcular_area()}")


# ------------------------------------------------------------
# 8. EXEMPLO PRÁTICO / PRACTICAL EXAMPLE
# ------------------------------------------------------------

class Pagamento:
    def processar(self, valor):
        raise NotImplementedError("Implemente o método processar().")


class PagamentoPix(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via PIX.")


class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} via cartão.")


class PagamentoDinheiro(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} em dinheiro.")


def realizar_pagamento(metodo, valor):
    metodo.processar(valor)


pagamentos = [
    PagamentoPix(),
    PagamentoCartao(),
    PagamentoDinheiro()
]

for pagamento in pagamentos:
    realizar_pagamento(pagamento, 150)


# ------------------------------------------------------------
# 9. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ------------------------------------------------------------

# EXERCÍCIO 1 / EXERCISE 1:
# Crie classes de animais com o mesmo método emitir_som().
# Create animal classes with the same emitir_som() method.

class Cachorro:
    def emitir_som(self):
        print("Au au!")


class Gato:
    def emitir_som(self):
        print("Miau!")


def fazer_som(animal):
    animal.emitir_som()


fazer_som(Cachorro())
fazer_som(Gato())


# EXERCÍCIO 2 / EXERCISE 2:
# Crie diferentes formas com o método calcular_area().
# Create different shapes with the calcular_area() method.

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * self.raio ** 2


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


formas = [Circulo(3), Retangulo(4, 5)]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")


# EXERCÍCIO 3 / EXERCISE 3:
# Crie diferentes tipos de pagamento com o método pagar().
# Create different payment types with the pagar() method.

class Pix:
    def pagar(self, valor):
        print(f"PIX: R$ {valor:.2f}")


class Cartao:
    def pagar(self, valor):
        print(f"Cartão: R$ {valor:.2f}")


def realizar_pagamento(metodo, valor):
    metodo.pagar(valor)


realizar_pagamento(Pix(), 100)
realizar_pagamento(Cartao(), 200)


# ------------------------------------------------------------
# 10. RESUMO / SUMMARY
# ------------------------------------------------------------

# Polimorfismo / Polymorphism:
# Mesmo método, diferentes comportamentos.
# Same method, different behaviors.

# Sobrescrita / Method overriding:
# A classe filha redefine um método herdado.
# The child class redefines an inherited method.

# Duck Typing:
# O objeto precisa oferecer o comportamento esperado,
# independentemente de sua classe.
# The object must provide the expected behavior,
# regardless of its class.

# Classe abstrata / Abstract class:
# Define uma estrutura que as classes filhas devem implementar.
# Defines a structure that child classes must implement.

# @abstractmethod:
# Define um método obrigatório nas classes concretas.
# Defines a required method in concrete classes.

# raise NotImplementedError:
# Indica que um método deve ser implementado em uma subclasse.
# Indicates that a method should be implemented in a subclass.

# PRINCIPAL IDEIA / MAIN IDEA:
# Diferentes objetos podem responder à mesma chamada de método
# de maneiras diferentes.
#
# Different objects can respond to the same method call
# in different ways.
