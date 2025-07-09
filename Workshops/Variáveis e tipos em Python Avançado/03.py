# O Python tem como classe base a classe object. Os demais herdam dessa classe


#Como uma simples soma de dois números pode tem uma complexidade associada???

resultado = 15 + 5
print(resultado)

#equivalente
x = 15
resultado = x + 5
print(resultado)


x = 15
resultado = x.__add__(5)  # Equivalente a 15 + 5 (dunder method __add__)
print(resultado)



# Operadores como Sintaxe Açucarada:
# Quando você escreve uma expressão como x + y, o interpretador Python a converte internamente em uma chamada ao método especial __add__ do objeto x.
# Ou seja, x + y é equivalente a x.__add__(y).

# Definição no Modelo de Dados:
# Essa associação entre operadores e métodos especiais está definida na especificação da linguagem Python (no Data Model).
# Cada operador tem um ou mais métodos associados:

# + → __add__ (e, se necessário, __radd__)
# - → __sub__ (e __rsub__)
# * → __mul__ (e __rmul__)


# A classe base object define algumas implementações padrão, mas, para tipos como int, float, str, etc., esses métodos são
# sobrescritos para realizar as operações apropriadas. 
# Assim, não é o object que "sabe" diretamente o que fazer com o +,
# mas sim a implementação específica da classe (por exemplo, int.__add__).
