
# ============================================================
# HERANÇA EM ORIENTAÇÃO A OBJETOS
# OBJECT-ORIENTED INHERITANCE (OOP)
# ============================================================

# 1. O QUE É HERANÇA? / WHAT IS INHERITANCE?
#
# Herança permite que uma classe (filha) reutilize atributos
# e métodos de outra classe (pai).
#
# Inheritance allows a class (child) to reuse attributes
# and methods from another class (parent).
#
# Classe pai = Parent class / Base class
# Classe filha = Child class / Derived class
#
# Vantagem / Advantage:
# Reutilização de código / Code reuse.


# ------------------------------------------------------------
# 2. HERANÇA SIMPLES / SINGLE INHERITANCE
# ------------------------------------------------------------

class Animal:  # Classe pai / Parent class
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("O animal está emitindo um som.")


class Cachorro(Animal):  # Classe filha / Child class
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")


cachorro = Cachorro("Rex")

cachorro.emitir_som()  # Método herdado / Inherited method
cachorro.latir()       # Método próprio / Own method


# ------------------------------------------------------------
# 3. FUNÇÃO SUPER() / SUPER() FUNCTION
# ------------------------------------------------------------

# super() permite acessar métodos da classe pai,
# especialmente seu inicializador __init__().
#
# super() allows accessing parent class methods,
# especially its __init__() initializer.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")


estudante = Estudante("Enzzo", 22, "Python")
estudante.apresentar()


# ------------------------------------------------------------
# 4. SOBRESCRITA DE MÉTODOS / METHOD OVERRIDING
# ------------------------------------------------------------

# A classe filha pode redefinir um método herdado.
# The child class can redefine an inherited method.

class Animal:
    def emitir_som(self):
        print("Som genérico de animal.")


class Gato(Animal):
    def emitir_som(self):
        print("Miau!")


gato = Gato()
gato.emitir_som()  # Executa o método sobrescrito / Calls overridden method


# ------------------------------------------------------------
# 5. HERANÇA MULTINÍVEL / MULTILEVEL INHERITANCE
# ------------------------------------------------------------

# Uma classe herda de outra que também herdou de uma terceira.
# A class inherits from another class that inherited from a third one.

class SerVivo:
    def respirar(self):
        print("Respirando...")


class Animal(SerVivo):
    def movimentar(self):
        print("O animal está se movimentando.")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


cachorro = Cachorro()

cachorro.respirar()
cachorro.movimentar()
cachorro.latir()


# ------------------------------------------------------------
# 6. HERANÇA MÚLTIPLA / MULTIPLE INHERITANCE
# ------------------------------------------------------------

# Uma classe pode herdar de mais de uma classe pai.
# A class can inherit from more than one parent class.

class Nadador:
    def nadar(self):
        print("Estou nadando!")


class Corredor:
    def correr(self):
        print("Estou correndo!")


class Atleta(Nadador, Corredor):
    pass


atleta = Atleta()
atleta.nadar()
atleta.correr()


# ------------------------------------------------------------
# 7. VERIFICAR HERANÇA / CHECKING INHERITANCE
# ------------------------------------------------------------

# isinstance() verifica se um objeto pertence a uma classe
# ou a uma classe ancestral.
#
# isinstance() checks whether an object belongs to a class
# or one of its parent classes.

class Veiculo:
    pass


class Carro(Veiculo):
    pass


carro = Carro()

print(isinstance(carro, Carro))    # True
print(isinstance(carro, Veiculo))  # True


# issubclass() verifica se uma classe herda de outra.
# issubclass() checks whether a class inherits from another.

print(issubclass(Carro, Veiculo))  # True


# ------------------------------------------------------------
# 8. EXEMPLO PRÁTICO / PRACTICAL EXAMPLE
# ------------------------------------------------------------

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R$ {self.salario:.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}")


gerente = Gerente("Carlos", 5000, "Tecnologia")
gerente.exibir_dados()


# ------------------------------------------------------------
# 9. EXERCÍCIOS RESOLVIDOS / SOLVED EXERCISES
# ------------------------------------------------------------

# EXERCÍCIO 1 / EXERCISE 1:
# Crie uma classe Veiculo e uma classe Carro que herde dela.
# Create a Vehicle class and a Car class that inherits from it.

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def ligar(self):
        print("Veículo ligado!")


class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.marca} está acelerando.")


meu_carro = Carro("Toyota")
meu_carro.ligar()
meu_carro.acelerar()


# EXERCÍCIO 2 / EXERCISE 2:
# Crie uma classe Pessoa e uma classe Professor que herde dela.
# Create a Person class and a Professor class that inherits from it.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia

    def apresentar(self):
        print(f"Professor: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matéria: {self.materia}")


professor = Professor("João", 35, "Programação")
professor.apresentar()


# EXERCÍCIO 3 / EXERCISE 3:
# Sobrescreva um método da classe pai na classe filha.
# Override a parent class method in the child class.

class Animal:
    def emitir_som(self):
        print("Som de animal.")


class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")


cachorro = Cachorro()
cachorro.emitir_som()


# ------------------------------------------------------------
# 10. RESUMO / SUMMARY
# ------------------------------------------------------------

# Herança / Inheritance:
# Reutiliza atributos e métodos de outra classe.
# Reuses attributes and methods from another class.

# super():
# Acessa métodos da classe pai.
# Accesses parent class methods.

# Sobrescrita / Overriding:
# Redefine um método herdado na classe filha.
# Redefines an inherited method in the child class.

# Herança simples / Single inheritance:
# Uma classe filha herda de uma classe pai.
# One child class inherits from one parent class.

# Herança multinível / Multilevel inheritance:
# Uma classe herda de outra classe que também herdou.
# A class inherits from another class that also inherited.

# Herança múltipla / Multiple inheritance:
# Uma classe herda de várias classes pai.
# A class inherits from multiple parent classes.

# isinstance():
# Verifica se um objeto pertence a uma classe ou ancestral.
# Checks whether an object belongs to a class or ancestor.

# issubclass():
# Verifica se uma classe herda de outra.
# Checks whether a class inherits from another.
