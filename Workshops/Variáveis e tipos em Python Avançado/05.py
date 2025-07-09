# Curiosidades

### Por que Dois Tipos Numéricos? (int vs. float)
# Inteiros (int):
#  - Representação: Precisão arbitrária – o tamanho pode aumentar conforme a necessidade.
#  - Vantagens: Sem erro de arredondamento, ideal para contagens e aritmética exata.

a = 123456789012345678901234567890
print(a * 2)

# Ponto Flutuante (float):
#  - Representação: Baseado no padrão IEEE 754 – usa 64 bits (na maioria dos casos).8 bytes
#  - Limitações: Erros de precisão devido à representação binária dos números decimais.

a = 0.1 + 0.2
print(a)           # Pode não imprimir exatamente 0.3
print(round(a, 2))


# ------------------------------------------------------------------------------------------------------

# Funcionamento Interno das Strings e a Ausência do Tipo char 
# Representação das Strings:
#  - Imutabilidade: Uma vez criada, a string não pode ser alterada.
#  - Unicode: Suporte completo para Unicode, possibilitando a representação de caracteres de diversos idiomas.
#  - Armazenamento: Internamente, as strings são arrays de códigos Unicode.


s = 'a'
s = 'aa'

# Por que não há um tipo char:
#     Em Python, um “caractere” é simplesmente uma string de tamanho 1.
#     Isso simplifica a linguagem e evita a necessidade de um tipo separado para caracteres.

letra = 'a'
print(type(letra))  # Saída: <class 'str'>
print(len(letra))   # Saída: 1


# Internamento de Strings: Strings curtas e/ou constantes podem ser “internadas” para melhorar a performance.

a = "python"
b = "python"
print(a is b)  # Pode resultar em True devido ao interning
# b = 'murilo'
# print(a is b)

import sys
print(sys.getrefcount("bsaihsdiahsdihaidhaidhaiusd"))