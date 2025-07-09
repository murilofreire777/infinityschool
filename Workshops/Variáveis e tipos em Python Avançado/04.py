# Linguagens estaticamente tipadas vs linguagens dinamicamente tipadas

# Copia por valor, int, str, float, bool, tuple
x = 5
y = x
x = 10
print(y)

#copia por referencia, list, dict, obj
a = [1,2,3]
b = a
a.pop()
print(b)