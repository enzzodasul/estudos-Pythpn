
# ============================================================
# EXERCÍCIO 1: CRIAR UMA CLASSE PESSOA
# EXERCISE 1: CREATE A PERSON CLASS
# ============================================================

# PT: Crie uma classe Pessoa com nome, idade e cidade.
# Crie também um método para apresentar essas informações.
#
# EN: Create a Person class with name, age, and city.
# Also create a method to display this information.

class Pessoa:

    # Construtor / Constructor
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    # Método de apresentação / Presentation method
    def apresentacao(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}.")


# Criando um objeto / Creating an object
pessoa1 = Pessoa("Enzo", 20, "Juiz de Fora")

# Chamando o método / Calling the method
pessoa1.apresentacao()

# Resultado / Output:
# Olá! Meu nome é Enzo, tenho 20 anos e moro em Juiz de Fora.


# ============================================================
# EXERCÍCIO 2: GERENCIAMENTO DE ESTOQUE
# EXERCISE 2: INVENTORY MANAGEMENT
# ============================================================

# PT: Crie uma classe Produto com nome, preço e quantidade.
# Adicione métodos para aumentar e diminuir o estoque.
#
# EN: Create a Product class with name, price, and quantity.
# Add methods to increase and decrease inventory.

class Produto:

    # Construtor / Constructor
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    # Aumentar estoque / Increase inventory
    def aumentar_estoque(self, quantidade):

        if quantidade <= 0:
            print("Informe uma quantidade válida.")
            return

        self.quantidade += quantidade

        print(f"Estoque aumentado! Quantidade atual: {self.quantidade}")

    # Diminuir estoque / Decrease inventory
    def diminuir_estoque(self, quantidade):

        if quantidade <= 0:
            print("Informe uma quantidade válida.")
            return

        if quantidade > self.quantidade:
            print("Estoque insuficiente!")
            return

        self.quantidade -= quantidade

        print(f"Estoque diminuído! Quantidade atual: {self.quantidade}")

    # Exibir informações / Display information
    def mostrar_produto(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade}")


# Criando um objeto / Creating an object
produto1 = Produto("Notebook", 3500.00, 10)

produto1.mostrar_produto()

# Adicionando 5 unidades / Adding 5 units
produto1.aumentar_estoque(5)

# Retirando 3 unidades / Removing 3 units
produto1.diminuir_estoque(3)

# Exibindo estoque atualizado / Displaying updated inventory
produto1.mostrar_produto()

# Resultado final / Final result:
# Produto: Notebook
# Preço: R$ 3500.00
# Quantidade em estoque: 12


# ============================================================
# EXERCÍCIO 3: JOGO DE RPG SIMPLES
# EXERCISE 3: SIMPLE RPG GAME
# ============================================================

# PT: Crie uma classe Jogador com nome, vida e poder.
# Crie métodos para atacar e verificar se está vivo.
#
# EN: Create a Player class with name, health, and power.
# Create methods to attack and check whether the player is alive.

class Jogador:

    # Construtor / Constructor
    def __init__(self, nome, vida, poder):
        self.nome = nome
        self.vida = vida
        self.poder = poder

    # Atacar outro jogador / Attack another player
    def atacar(self, outro_jogador):

        if not self.esta_vivo():
            print(f"{self.nome} não pode atacar porque está derrotado!")
            return

        if not outro_jogador.esta_vivo():
            print(f"{outro_jogador.nome} já está derrotado!")
            return

        outro_jogador.vida -= self.poder

        # Impedir que a vida fique negativa
        # Prevent health from becoming negative
        outro_jogador.vida = max(0, outro_jogador.vida)

        print(f"{self.nome} atacou {outro_jogador.nome}!")
        print(f"Dano causado: {self.poder}")
        print(f"Vida restante de {outro_jogador.nome}: {outro_jogador.vida}")

    # Verificar se o jogador está vivo / Check if the player is alive
    def esta_vivo(self):

        return self.vida > 0

    # Exibir status / Display status
    def mostrar_status(self):

        print(f"Jogador: {self.nome}")
        print(f"Vida: {self.vida}")
        print(f"Poder: {self.poder}")

        if self.esta_vivo():
            print("Status: Vivo")
        else:
            print("Status: Derrotado")


# Criando jogadores / Creating players
jogador1 = Jogador("Guerreiro", 100, 25)
jogador2 = Jogador("Mago", 80, 30)

# Exibindo status inicial / Displaying initial status
jogador1.mostrar_status()
jogador2.mostrar_status()

# Guerreiro ataca o mago / Warrior attacks the wizard
jogador1.atacar(jogador2)

# Mago ataca o guerreiro / Wizard attacks the warrior
jogador2.atacar(jogador1)

# Exibindo status final / Displaying final status
jogador1.mostrar_status()
jogador2.mostrar_status()
