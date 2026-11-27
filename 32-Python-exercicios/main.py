
# ============================================================
# EXERCÍCIOS DE HERANÇA / INHERITANCE EXERCISES
# ============================================================


# ------------------------------------------------------------
# EXERCÍCIO 1: HERANÇA DE VEÍCULOS
# EXERCISE 1: VEHICLE INHERITANCE
# ------------------------------------------------------------

# Classe base / Base class
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


# Classe derivada / Derived class
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_portas):
        super().__init__(marca, modelo, ano)
        self.quantidade_portas = quantidade_portas

    def exibir_portas(self):
        print(f"Quantidade de portas: {self.quantidade_portas}")


# Classe derivada / Derived class
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_cilindradas(self):
        print(f"Cilindradas: {self.cilindradas} cc")


# Testes / Tests
carro = Carro("Toyota", "Corolla", 2024, 4)
moto = Moto("Honda", "CB 500", 2023, 500)

print("=== CARRO ===")
carro.exibir_informacoes()
carro.exibir_portas()

print("\n=== MOTO ===")
moto.exibir_informacoes()
moto.exibir_cilindradas()


# ------------------------------------------------------------
# EXERCÍCIO 2: HERANÇA DE CONTA BANCÁRIA
# EXERCISE 2: BANK ACCOUNT INHERITANCE
# ------------------------------------------------------------

# Classe base / Base class
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def consultar_saldo(self):
        print(f"Saldo: R$ {self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("O valor deve ser positivo.")


# Classe derivada / Derived class
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def utilizar_limite(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Operação de R$ {valor:.2f} realizada!")
        else:
            print("Limite insuficiente ou valor inválido.")


# Classe derivada / Derived class
class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        rendimento = self.saldo * (self.taxa_rendimento / 100)
        self.saldo += rendimento
        print(f"Rendimento aplicado: R$ {rendimento:.2f}")


# Testes / Tests
conta_corrente = ContaCorrente("Enzzo", 1000, 500)
conta_poupanca = ContaPoupanca("Maria", 2000, 1.5)

print("\n=== CONTA CORRENTE ===")
print(f"Titular: {conta_corrente.titular}")
conta_corrente.utilizar_limite(1200)
conta_corrente.consultar_saldo()

print("\n=== CONTA POUPANÇA ===")
print(f"Titular: {conta_poupanca.titular}")
conta_poupanca.aplicar_rendimento()
conta_poupanca.consultar_saldo()


# ------------------------------------------------------------
# EXERCÍCIO 3: HERANÇA DE ANIMAIS
# EXERCISE 3: ANIMAL INHERITANCE
# ------------------------------------------------------------

# Classe base / Base class
class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")


# Classe derivada / Derived class
class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo: Au au!")


# Classe derivada / Derived class
class Gato(Animal):
    def miar(self):
        print(f"{self.nome} está miando: Miau!")


# Testes / Tests
cachorro = Cachorro("Rex", "Doméstico")
gato = Gato("Mimi", "Doméstico")

print("\n=== CACHORRO ===")
cachorro.exibir_informacoes()
cachorro.latir()

print("\n=== GATO ===")
gato.exibir_informacoes()
gato.miar()


# ============================================================
# RESUMO / SUMMARY
# ============================================================

# Herança / Inheritance:
# Permite reutilizar atributos e métodos de uma classe base.
# Allows reusing attributes and methods from a base class.

# super():
# Chama o inicializador ou métodos da classe pai.
# Calls the initializer or methods from the parent class.

# Classe base / Base class:
# Classe que fornece atributos e métodos para outras classes.
# Class that provides attributes and methods to other classes.

# Classe derivada / Derived class:
# Classe que herda características de outra classe.
# Class that inherits features from another class.

# Método específico / Specific method:
# Método criado dentro de uma classe derivada.
# Method created inside a derived class.
