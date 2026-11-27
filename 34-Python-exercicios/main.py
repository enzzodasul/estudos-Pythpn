
# ============================================================
# EXERCÍCIOS DE POLIMORFISMO
# POLYMORPHISM EXERCISES
# ============================================================


# ------------------------------------------------------------
# EXERCÍCIO 1: POLIMORFISMO COM FORMAS GEOMÉTRICAS
# EXERCISE 1: POLYMORPHISM WITH GEOMETRIC SHAPES
# ------------------------------------------------------------

# Classe base / Base class
class Forma:
    def calcular_area(self):
        pass


# Classe derivada / Derived class
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


# Classe derivada / Derived class
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)


# Testes / Tests
retangulo = Retangulo(5, 4)
circulo = Circulo(3)

formas = [retangulo, circulo]

for forma in formas:
    print(f"Área: {forma.calcular_area():.2f}")

# Resultado esperado / Expected output:
# Área: 20.00
# Área: 28.26


# ------------------------------------------------------------
# EXERCÍCIO 2: POLIMORFISMO COM ANIMAIS
# EXERCISE 2: POLYMORPHISM WITH ANIMALS
# ------------------------------------------------------------

# Classe base / Base class
class Animal:
    def emitir_som(self):
        pass


# Classe derivada / Derived class
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au! O cachorro está latindo.")


# Classe derivada / Derived class
class Gato(Animal):
    def emitir_som(self):
        print("Miau! O gato está miando.")


# Testes / Tests
cachorro = Cachorro()
gato = Gato()

animais = [cachorro, gato]

for animal in animais:
    animal.emitir_som()

# Resultado esperado / Expected output:
# Au au! O cachorro está latindo.
# Miau! O gato está miando.


# ------------------------------------------------------------
# EXERCÍCIO 3: POLIMORFISMO COM VEÍCULOS
# EXERCISE 3: POLYMORPHISM WITH VEHICLES
# ------------------------------------------------------------

# Classe base / Base class
class Veiculo:
    def acelerar(self):
        pass


# Classe derivada / Derived class
class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando gradualmente.")


# Classe derivada / Derived class
class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando rapidamente.")


# Testes / Tests
carro = Carro()
moto = Moto()

veiculos = [carro, moto]

for veiculo in veiculos:
    veiculo.acelerar()

# Resultado esperado / Expected output:
# O carro está acelerando gradualmente.
# A moto está acelerando rapidamente.


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# Polimorfismo / Polymorphism:
# Permite que diferentes classes implementem o mesmo método
# com comportamentos diferentes.
#
# Allows different classes to implement the same method
# with different behaviors.

# Classe base / Base class:
# Fornece uma estrutura comum para as classes derivadas.
# Provides a common structure for derived classes.

# Classe derivada / Derived class:
# Herda características da classe base e pode sobrescrever métodos.
# Inherits features from the base class and can override methods.

# Sobrescrita / Method overriding:
# A classe filha implementa sua própria versão de um método.
# The child class implements its own version of a method.

# PRINCIPAL IDEIA / MAIN IDEA:
# Mesmo método + objetos diferentes = comportamentos diferentes.
# Same method + different objects = different behaviors.
