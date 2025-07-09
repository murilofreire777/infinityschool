#Definição de função

#Organização de código
#Reuso
#Documentação

#Parametros e retornos (posicional, nomeado, retorno múltiplo)

# *args e **kwargs
# *args -> função que pode receber N parâmetros posicionais
# *args é tupla

def somatorio(val, *args):
    resultado = val
    for value in args:
        resultado += value
    return resultado 

print(somatorio(1,2,3,4,5))

# **kwargs ->  -> função que pode receber N parâmetros nomeados
# **kwargs é um dicionário

def valor_teste(val, **kwargs):
    resultado = 0
    if 'chave' in kwargs:
        resultado = val * kwargs['chave']
    else:
        resultado = val * 2
    return resultado 

print(valor_teste(10, chave=20))

#Recursividade
#Consiste em uma função invocar a si mesma ou funções invocarem umas às outras
# 4! => 4 x 3 x 2 x 1
# 4! => 4 x 3! => 4 x 3 x 2! ....

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

print(fatorial(6))

#Inner functions

#High order functions e Closures
#High order -> Funções que recebem funções como parâmetros ou retornam outras funções
#Closures -> Funções que retém seu estado interno após serem retornadas por outras funções
def gera_multiplicador(factor):
    def multiplicar(n):
        return n * factor
    return multiplicar
dobra = gera_multiplicador(2)
triplica = gera_multiplicador(3)

dobra(4) #8
dobra(5) #10
triplica(4) #12
triplica(5) #15

#List comprehension
#Cria uma nova lista a partir de uma lista existente.
#É um substituto do "for" + "if" ou da função 'filter' ou 'map'
#Sintaxe: 
#newlist = [expression for item in iterable if condition == True]

frutas = ["maçã", "banana", "uva", "laranja", "manga"]
frutas_filtradas = []

#somente frutas contendo a letra 'n'
for x in frutas:
  if "n" in x:
    frutas_filtradas.append(x)

#equivalente
frutas_filtradas = [x for x in frutas if "n" in x]

print(frutas_filtradas)

#sem o 'if', todas as frutas em maiúsculo
frutas_maiusculas = [x.upper() for x in frutas]

print(frutas_maiusculas)

#A expressão inicial pode ser também um 'if'
#Mantém 'banana' e troca as outras frutas por string vazia
newlist = [x if x == "banana" else "" for x in frutas]

#Funções lambda
#Função anônima de uma linha somente
#Pode receber vários argumentos mas contém somente uma expressão
x = lambda a, b : a * b
print(x(5, 6))

