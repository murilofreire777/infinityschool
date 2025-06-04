#1. Crie uma função que receba um número variado de argumentos numéricos e retorne a soma desses números
def somatorio(*args):
    resultado = 0
    for value in args:
        resultado += value
    return resultado

print(somatorio(1,2,3,4,5))

#2. Modifique a função do exercício 1 para, caso a chave 'multi' exista no kwargs, retorne a soma vezes esse valor
def somatorio_multi(*args, **kwargs):
    resultado = 0
    for value in args:
        resultado += value
    if 'multi' in kwargs:
        return resultado * kwargs['multi']
    else:
        return resultado

print(somatorio_multi(1,2,3,4,5,multi=10))

#3. Crie uma função recursiva que calcule a sequencia de Fibonacci para um número N
# A sequência de Fibinacci é realizada de modo que cada número é a soma dos dois anteriores
# 1 1 2 3 5 8
def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)
print(f(4))

#4. Crie uma função que retorne uma Closure para potência N de um número
def gera_expoente(pot):
    def potencia(base):
        return base ** pot
    return potencia
quadrado = gera_expoente(2)
cubo = gera_expoente(3)
print(quadrado(4)) #16
print(quadrado(5)) #25
print(cubo(4)) #64
print(cubo(5)) #625


#5. Use list comprehension para criar uma nova lista a partir da lista abaixo contendo apenas os números ímpares
#[0, 3, -4, -1, 2, 10, 5, 7]
lista = [0, 3, -4, -1, 2, 10, 5, 7]
lista_impares = [x for x in lista if x % 2 == 1]
print(lista_impares)

#6. Combine list comprehension com uma função lambda para obter o quadrado do dobro dos elementos da lista do exercício anterior
quad_double = lambda x : (2*x)**2
lista = [0, 3, -4, -1, 2, 10, 5, 7]
lista_impares = [ quad_double(x) for x in lista]
print(lista_impares)

#7. Modifique o item 4 para utilizar uma função lambda
def gera_expoente(pot):
    potencia = lambda base : base ** pot
    return potencia
quadrado = gera_expoente(2)
cubo = gera_expoente(3)
print(quadrado(4)) #16
print(quadrado(5)) #25
print(cubo(4)) #64
print(cubo(5)) #625
