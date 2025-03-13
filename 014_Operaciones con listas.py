"""Practica No. 14
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# La vida al interior de las listas
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

# Rebanadas Poderosas
rebanada = lista[1:4]
print("Rebanada de la lista (índices 1 a 3):", rebanada)

# Rebanadas – índices negativos
rebanada_negativa = lista[-3:-1]
print("Rebanada con índices negativos (últimos tres elementos):", rebanada_negativa)

# Los operadores in y not in
print("¿Está el número 3 en la lista?", 3 in lista) # True
print("¿No está el número 6 en la lista?", 6 not in lista) # True

# Programa 1: Sumar todos los elementos de la lista
suma = sum(lista)
print("Suma de todos los elementos de la lista:", suma)

# Programa 2: Encontrar el elemento más grande de la lista
maximo = max(lista)
print("Elemento más grande de la lista:", maximo)

# Programa 3: Invertir la lista
lista_invertida = lista[::-1]
print("Lista invertida:", lista_invertida)

# Programa 4: Valor mayor en la lista
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

