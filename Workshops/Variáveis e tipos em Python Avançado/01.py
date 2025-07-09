# Definição e Natureza:

# Em Python, variáveis não são “caixas” fixas na memória onde os valores são armazenados; elas são nomes (rótulos) que fazem referência a objetos.

a = 10        # 'a' referencia um objeto do tipo int com valor 10
b = "Olá"     # 'b' referencia um objeto do tipo str com valor "Olá"

# O TIPO É A CLASSE!


# Em linguagens com tipagem estática (como C ou Java), as variáveis são declaradas com um tipo fixo e a memória é alocada diretamente para esse tipo.
# Em Python, não há declaração explícita de tipo. Os nomes apenas apontam para objetos e o tipo é determinado em tempo de execução.



# Unificação do Modelo de Dados:
# Em Python, todos os elementos — sejam números, strings, listas, funções, classes, etc. — são objetos.
#  Isso significa que cada entidade possui:

#  - Um tipo (ou classe) que define seu comportamento e propriedades.
#  - Um estado (por exemplo, para um número, o valor armazenado).
#  - Uma identidade (que pode ser verificada com a função id(), indicando, em geral, o endereço de memória onde o objeto está armazenado).

c = 42 # você está criando um objeto do tipo int que contém o valor 42, e a variável 'c' se torna uma referência a esse objeto.


### Então o nome (referência) de uma variável é uma coisa e seu conteúdo (objeto) é outra?


# Armazenamento no Heap:
# Tanto os objetos (como números, strings, listas etc.) quanto os dicionários que compõem os namespaces são alocados no heap.

# Objetos: São criados dinamicamente e armazenados no heap.
# Namespaces (dicionários): Esses dicionários são objetos em si e, portanto, também vivem no heap.
#  Eles contêm as associações entre nomes (as chaves) e os objetos.


# Namespaces:
# Um namespace é basicamente um mapeamento que associa nomes (strings) a objetos. 
# Existem vários tipos de namespaces em Python, como:

# Global: O namespace do módulo, onde as variáveis definidas no escopo global ficam armazenadas.
# Local: O namespace dentro de uma função ou método, que contém as variáveis locais.
# Built-in: O namespace que contém os nomes integrados do Python (como len, print, etc.).
# Cada namespace é, na prática, um dicionário. 


x = 10
y = "Python"

print(globals())  # Mostra um dicionário com os nomes e os objetos correspondentes










#--------------------------------------------------------------------------------------------------

# Binding de Nomes a Objetos:
# Atribuir um valor a uma variável em Python é vincular o nome a um objeto. Esse processo é chamado de binding.

x = [1, 2, 3]  # 'x' passa a referenciar uma lista

nome = 'João' # A variável 'nome' passa a referenciar o objeto do tipo string (str) cujo valor é 'João'













#--------------------------------------------------------------------------------------------------

# Reatribuição e Mudança de Tipo:
# Uma vez criado, o nome pode ser reatribuído para referenciar outro objeto, mesmo que seja de tipo diferente.

a = 10       # 'a' referencia um inteiro
a = "dez"    # Agora, 'a' referencia uma string; o binding anterior é descartado (se não houver outras referências)


#--------------------------------------------------------------------------------------------------



