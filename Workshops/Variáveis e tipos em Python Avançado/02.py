# Características dos objects

#--------------------------------------------------------------------------------------------------

# Imutabilidade vs. Mutabilidade dos Objetos
# Objetos Imutáveis:
# Tipos como inteiros, floats, strings e tuplas são imutáveis. Isso significa que, uma vez criado, o objeto não pode ser alterado.
# Qualquer operação que “modifique” um objeto imutável, na verdade, cria um novo objeto.



s = "python"
s_modificado = s.upper()  # Cria uma nova string; 's' permanece inalterada.


# Objetos Mutáveis:
# Tipos como listas, dicionários e conjuntos podem ser modificados após sua criação.

lista = [1, 2, 3]
lista.append(4)  # A lista é alterada, mantendo a mesma identidade de objeto.


#--------------------------------------------------------------------------------------------------

# Identidade dos Objetos e a Função id()

# Identidade de Objeto:
# - Em Python, cada objeto possui uma identidade única, que pode ser obtida através da função id().
# - Essa identidade geralmente representa o endereço de memória onde o objeto está armazenado.

x = 100
y = 100
y = 101
print(id(x), id(y))
print(x is y)  # 'is' verifica se ambas as variáveis apontam para o mesmo objeto.

# Nota: Para certos tipos e valores (como inteiros pequenos), o Python implementa caching
# (por exemplo, para valores entre -5 e 256), de modo que variáveis com o mesmo valor podem,
# na prática, referenciar o mesmo objeto.

#ISSO NÃO FAZ DIFERENÇA NO DIA A DIA DO DESENVOLVEDOR!

# --------------------------------------------------------------------------------
#Coletor de lixo
# Quando um objeto deixa de ser referenciado, ele será descartado