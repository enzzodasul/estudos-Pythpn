
# ============================================================
# FUNÇÕES EM PYTHON — PARTE 2
# PYTHON FUNCTIONS — PART 2
# ============================================================


# ============================================================
# 1. FUNÇÕES LAMBDA
# 1. LAMBDA FUNCTIONS
# ============================================================

# PT: Lambda cria funções pequenas e anônimas em uma única expressão.
# EN: Lambda creates small anonymous functions in a single expression.

# Função tradicional / Traditional function
def somar(a, b):
    return a + b

print(somar(10, 5))  # 15

# Função lambda / Lambda function
somar_lambda = lambda a, b: a + b

print(somar_lambda(10, 5))  # 15


# ============================================================
# 2. SINTAXE DA LAMBDA
# 2. LAMBDA SYNTAX
# ============================================================

# PT: lambda recebe parâmetros e retorna uma expressão.
# EN: lambda receives parameters and returns an expression.

# lambda parâmetros: expressão

dobro = lambda numero: numero * 2
print(dobro(5))  # 10

quadrado = lambda numero: numero ** 2
print(quadrado(4))  # 16

# Lambda com um parâmetro / Lambda with one parameter
triplo = lambda numero: numero * 3
print(triplo(7))  # 21


# ============================================================
# 3. LAMBDA COM VÁRIOS PARÂMETROS
# 3. LAMBDA WITH MULTIPLE PARAMETERS
# ============================================================

multiplicar = lambda a, b: a * b
print(multiplicar(4, 5))  # 20

calcular_media = lambda nota1, nota2: (nota1 + nota2) / 2
print(calcular_media(8, 10))  # 9.0


# ============================================================
# 4. LAMBDA COM CONDICIONAL
# 4. LAMBDA WITH CONDITIONAL
# ============================================================

# PT: Podemos usar if e else dentro de uma expressão lambda.
# EN: We can use if and else inside a lambda expression.

verificar_idade = lambda idade: "Maior de idade" if idade >= 18 else "Menor de idade"

print(verificar_idade(20))
print(verificar_idade(15))

# Verificar par ou ímpar / Check even or odd
par_ou_impar = lambda numero: "Par" if numero % 2 == 0 else "Ímpar"

print(par_ou_impar(8))
print(par_ou_impar(7))


# ============================================================
# 5. FUNÇÕES ANÔNIMAS
# 5. ANONYMOUS FUNCTIONS
# ============================================================

# PT: Uma função anônima é uma função sem nome.
# EN: An anonymous function is a function without a name.

# Lambda é a maneira mais comum de criar funções anônimas.
# Lambda is the most common way to create anonymous functions.

print((lambda x: x + 10)(5))  # 15


# ============================================================
# 6. FUNÇÕES RECURSIVAS
# 6. RECURSIVE FUNCTIONS
# ============================================================

# PT: Uma função recursiva chama a si mesma.
# EN: A recursive function calls itself.

# Exemplo: contagem regressiva / Example: countdown

def contagem_regressiva(numero):
    if numero <= 0:
        print("Fim!")
        return

    print(numero)
    contagem_regressiva(numero - 1)


contagem_regressiva(5)

# Saída / Output:
# 5
# 4
# 3
# 2
# 1
# Fim!


# ============================================================
# 7. CASO BASE DA RECURSÃO
# 7. BASE CASE OF RECURSION
# ============================================================

# PT: O caso base determina quando a recursão deve parar.
# EN: The base case determines when recursion must stop.

def exemplo_recursivo(numero):
    if numero == 0:  # Caso base / Base case
        return

    print(numero)
    exemplo_recursivo(numero - 1)


exemplo_recursivo(3)

# IMPORTANTE / IMPORTANT:
# PT: Sem caso base, a função pode entrar em recursão infinita.
# EN: Without a base case, the function can recurse indefinitely.


# ============================================================
# 8. FATORIAL COM RECURSÃO
# 8. FACTORIAL WITH RECURSION
# ============================================================

# PT: O fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.
# EN: The factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1

    return numero * fatorial(numero - 1)


print(fatorial(5))  # 120


# ============================================================
# 9. FATORIAL COM LOOP
# 9. FACTORIAL WITH A LOOP
# ============================================================

# PT: Também podemos calcular o fatorial sem recursão.
# EN: We can also calculate factorial without recursion.

def fatorial_loop(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado *= i

    return resultado


print(fatorial_loop(5))  # 120


# ============================================================
# 10. SEQUÊNCIA DE FIBONACCI
# 10. FIBONACCI SEQUENCE
# ============================================================

# PT: Cada número é a soma dos dois anteriores.
# EN: Each number is the sum of the two previous numbers.

def fibonacci(numero):
    if numero <= 1:
        return numero

    return fibonacci(numero - 1) + fibonacci(numero - 2)


print(fibonacci(6))  # 8


# ============================================================
# 11. RECURSÃO COM LISTAS
# 11. RECURSION WITH LISTS
# ============================================================

def somar_lista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + somar_lista(lista[1:])


numeros = [10, 20, 30, 40]

print(somar_lista(numeros))  # 100


# ============================================================
# 12. FUNÇÕES DE ALTA ORDEM
# 12. HIGHER-ORDER FUNCTIONS
# ============================================================

# PT: Uma função de alta ordem recebe outra função como argumento
# ou retorna uma função.
# EN: A higher-order function receives another function as an argument
# or returns a function.

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)


def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


print(aplicar_operacao(5, 3, somar))       # 8
print(aplicar_operacao(5, 3, multiplicar)) # 15


# ============================================================
# 13. MAP()
# 13. MAP()
# ============================================================

# PT: map() aplica uma função a cada elemento de um iterável.
# EN: map() applies a function to each element of an iterable.

numeros = [1, 2, 3, 4, 5]

dobros = list(map(lambda numero: numero * 2, numeros))

print(dobros)  # [2, 4, 6, 8, 10]


# Usando função tradicional / Using a regular function
def dobrar(numero):
    return numero * 2


dobros = list(map(dobrar, numeros))

print(dobros)


# ============================================================
# 14. FILTER()
# 14. FILTER()
# ============================================================

# PT: filter() seleciona elementos que passam em uma condição.
# EN: filter() selects elements that satisfy a condition.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

pares = list(filter(lambda numero: numero % 2 == 0, numeros))

print(pares)  # [2, 4, 6, 8]

# Filtrar números maiores que 5 / Filter numbers greater than 5
maiores = list(filter(lambda numero: numero > 5, numeros))

print(maiores)  # [6, 7, 8]


# ============================================================
# 15. REDUCE()
# 15. REDUCE()
# ============================================================

# PT: reduce() acumula os elementos de um iterável em um resultado.
# EN: reduce() accumulates iterable elements into a single result.

# PT: reduce() precisa ser importado do módulo functools.
# EN: reduce() must be imported from the functools module.

from functools import reduce

numeros = [1, 2, 3, 4, 5]

soma_total = reduce(lambda acumulador, numero: acumulador + numero, numeros)

print(soma_total)  # 15

produto_total = reduce(lambda acumulador, numero: acumulador * numero, numeros)

print(produto_total)  # 120


# ============================================================
# 16. SORTED() COM LAMBDA
# 16. SORTED() WITH LAMBDA
# ============================================================

# PT: sorted() organiza os elementos.
# O parâmetro key permite definir o critério de ordenação.
# EN: sorted() sorts elements.
# The key parameter lets us define the sorting criterion.

nomes = ["Carlos", "Ana", "Beatriz", "João"]

ordenados = sorted(nomes, key=lambda nome: len(nome))

print(ordenados)

# Ordenar em ordem decrescente / Sort in descending order
ordenados = sorted(nomes, key=lambda nome: len(nome), reverse=True)

print(ordenados)


# ============================================================
# 17. LAMBDA COM DICIONÁRIOS
# 17. LAMBDA WITH DICTIONARIES
# ============================================================

pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 18},
    {"nome": "Beatriz", "idade": 30}
]

# Ordenar pelo valor da idade / Sort by age
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])

print(pessoas_ordenadas)


# ============================================================
# 18. FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES
# 18. FUNCTIONS THAT RETURN OTHER FUNCTIONS
# ============================================================

def criar_multiplicador(fator):

    def multiplicar(numero):
        return numero * fator

    return multiplicar


dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(dobrar(10))     # 20
print(triplicar(10))  # 30


# ============================================================
# 19. CLOSURES
# 19. CLOSURES
# ============================================================

# PT: Closure é uma função que mantém acesso a variáveis
# do escopo em que foi criada, mesmo após esse escopo terminar.
# EN: A closure is a function that retains access to variables
# from its enclosing scope, even after that scope has finished.

def criar_saudacao(nome):

    def saudar():
        return f"Olá, {nome}!"

    return saudar


mensagem = criar_saudacao("Enzo")

print(mensagem())  # Olá, Enzo!


# ============================================================
# 20. NONLOCAL
# 20. NONLOCAL
# ============================================================

# PT: nonlocal permite alterar uma variável de uma função externa.
# EN: nonlocal allows changing a variable from an enclosing function.

def criar_contador():

    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar


contador = criar_contador()

print(contador())  # 1
print(contador())  # 2
print(contador())  # 3


# ============================================================
# 21. DECORADORES
# 21. DECORATORS
# ============================================================

# PT: Decoradores modificam ou ampliam o comportamento de funções.
# EN: Decorators modify or extend the behavior of functions.

def meu_decorador(funcao):

    def wrapper():
        print("Antes da função / Before the function")
        funcao()
        print("Depois da função / After the function")

    return wrapper


@meu_decorador
def mostrar_mensagem():
    print("Executando a função! / Running the function!")


mostrar_mensagem()


# ============================================================
# 22. DECORADORES COM ARGUMENTOS
# 22. DECORATORS WITH ARGUMENTS
# ============================================================

def decorador(funcao):

    def wrapper(*args, **kwargs):
        print("Iniciando / Starting")

        resultado = funcao(*args, **kwargs)

        print("Finalizando / Finishing")

        return resultado

    return wrapper


@decorador
def apresentar(nome):
    return f"Olá, {nome}!"


print(apresentar("Enzo"))


# ============================================================
# 23. FUNÇÕES GERADORAS — YIELD
# 23. GENERATOR FUNCTIONS — YIELD
# ============================================================

# PT: yield produz valores um por vez, mantendo o estado da função.
# EN: yield produces values one at a time, preserving function state.

def gerar_numeros():
    yield 1
    yield 2
    yield 3


for numero in gerar_numeros():
    print(numero)


# Gerador com loop / Generator with a loop
def contar_ate(limite):

    for numero in range(1, limite + 1):
        yield numero


for numero in contar_ate(5):
    print(numero)


# ============================================================
# 24. FUNÇÕES RECURSIVAS VS ITERATIVAS
# 24. RECURSIVE VS ITERATIVE FUNCTIONS
# ============================================================

# Recursiva / Recursive
def somar_recursivo(numero):
    if numero <= 0:
        return 0

    return numero + somar_recursivo(numero - 1)


# Iterativa / Iterative
def somar_iterativo(numero):
    total = 0

    for i in range(1, numero + 1):
        total += i

    return total


print(somar_recursivo(5))  # 15
print(somar_iterativo(5)) # 15


# ============================================================
# 25. BOAS PRÁTICAS
# 25. BEST PRACTICES
# ============================================================

# PT: Use lambda para operações pequenas e simples.
# EN: Use lambda for small and simple operations.

dobro = lambda numero: numero * 2


# PT: Use def para funções maiores ou com várias instruções.
# EN: Use def for larger functions or functions with multiple statements.

def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto


# PT: Sempre defina um caso base nas funções recursivas.
# EN: Always define a base case in recursive functions.

# PT: Evite recursão desnecessária em tarefas que podem usar loops.
# EN: Avoid unnecessary recursion in tasks that can use loops.

# PT: Dê nomes claros às funções.
# EN: Use clear function names.


# ============================================================
# 26. EXERCÍCIOS RESOLVIDOS
# 26. SOLVED EXERCISES
# ============================================================

# EXERCÍCIO 1 / EXERCISE 1
# Crie uma lambda que calcule o cubo de um número.
# Create a lambda that calculates the cube of a number.

cubo = lambda numero: numero ** 3

print(cubo(3))  # 27


# EXERCÍCIO 2 / EXERCISE 2
# Crie uma função recursiva que conte de 1 até N.
# Create a recursive function that counts from 1 to N.

def contar(numero):

    if numero <= 0:
        return

    contar(numero - 1)
    print(numero)


contar(5)


# EXERCÍCIO 3 / EXERCISE 3
# Use filter() para encontrar números ímpares.
# Use filter() to find odd numbers.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

impares = list(filter(lambda numero: numero % 2 != 0, numeros))

print(impares)  # [1, 3, 5, 7, 9]


# EXERCÍCIO 4 / EXERCISE 4
# Use map() para transformar temperaturas de Celsius em Fahrenheit.
# Use map() to convert Celsius temperatures to Fahrenheit.

celsius = [0, 10, 20, 30]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0]


# EXERCÍCIO 5 / EXERCISE 5
# Use reduce() para encontrar o maior número de uma lista.
# Use reduce() to find the largest number in a list.

numeros = [12, 45, 7, 89, 23]

maior = reduce(lambda a, b: a if a > b else b, numeros)

print(maior)  # 89


# ============================================================
# 27. EXERCÍCIOS PARA PRATICAR
# 27. PRACTICE EXERCISES
# ============================================================

# 1. Crie uma lambda que calcule a metade de um número.
#    Create a lambda that calculates half of a number.

# 2. Crie uma função recursiva que calcule a soma de 1 até N.
#    Create a recursive function that calculates the sum from 1 to N.

# 3. Use map() para elevar todos os números de uma lista ao quadrado.
#    Use map() to square every number in a list.

# 4. Use filter() para selecionar números maiores que 10.
#    Use filter() to select numbers greater than 10.

# 5. Use reduce() para multiplicar todos os números de uma lista.
#    Use reduce() to multiply all numbers in a list.

# 6. Crie uma função que retorne outra função multiplicadora.
#    Create a function that returns another multiplier function.

# 7. Crie um gerador que produza números pares até N.
#    Create a generator that produces even numbers up to N.

# 8. Crie um decorador que mostre uma mensagem antes de executar
#    uma função.
#    Create a decorator that displays a message before executing
#    a function.


# ============================================================
# 28. RESUMO GERAL
# 28. GENERAL SUMMARY
# ============================================================

# lambda      -> Função anônima / Anonymous function
# Recursão    -> Função que chama a si mesma / Function calling itself
# Caso base   -> Condição de parada / Stopping condition
# map()       -> Transforma elementos / Transforms elements
# filter()    -> Filtra elementos / Filters elements
# reduce()    -> Acumula elementos / Accumulates elements
# sorted()    -> Ordena elementos / Sorts elements
# Closure     -> Mantém acesso ao escopo externo / Retains outer scope
# nonlocal    -> Altera variável do escopo externo / Changes enclosing variable
# Decorator   -> Modifica comportamento / Modifies behavior
# yield       -> Produz valores de um gerador / Produces generator values
