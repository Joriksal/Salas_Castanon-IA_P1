"""Practica No. 12
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Listas - Indexación de listas

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros)  

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros)  

numeros[1] = numeros[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numeros)  

# Listas - Acceso al contenido de las listas

# Acceso a un numero de la lista

print(numeros[0]) # Accediendo al primer elemento de la lista.

print("\nLongitud de la lista:", len(numeros))  # Imprimiendo la longitud de la lista.

print(numeros) 

# Listas - Eliminando elementos de una lista

del numeros[1] # Eliminando el segundo elemento de la lista.
print(len(numeros)) 
print(numeros) 

# Listas - Indices negativos

print(numeros[-1]) # Imprimiendo el ultimo elemento de la lista.

print(numeros[-2]) # Imprimiendo el penultimo elemento de la lista.

# Listas - Funciones vs Metodos

print(len(numeros)) 
print(numeros) 

numeros.append(4) # Agregando un elemento a la lista.

print(len(numeros)) 
print(numeros)

numeros.insert(0, 222) # Insertando un elemento en la posicion 0 de la lista.
print(len(numeros)) 
print(numeros) 

# Listas - Uso de las listas

print("Suma de los elementos de una lista\n")

lista = [10, 1, 8, 3, 5]
total = 0

for i in range(len(lista)):
    total += lista[i]

print(total)

# Listas - Ordenamiento de listas

print("Ordenamiento de listas\n")

largo = len(lista)

for i in range(largo // 2):
    lista[i], lista[largo - i - 1] = lista[largo - i - 1], lista[i]
 
print(lista)
