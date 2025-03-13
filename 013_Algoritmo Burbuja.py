"""Practica No. 13
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Algoritmo de ordenamiento burbuja

mi_lista = [8, 10, 6, 2, 4]  # lista a ordenar
print(mi_lista) 
intercambiado = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while intercambiado:
    intercambiado = False  # no hay intercambios hasta ahora
    for i in range(len(mi_lista) - 1):
        if mi_lista[i] > mi_lista[i + 1]:
            intercambiado = True  # ¡ocurrió el intercambio!
            mi_lista[i], mi_lista[i + 1] = mi_lista[i + 1], mi_lista[i]
 
print(mi_lista)

# Salida esperada: [2, 4, 6, 8, 10]

# Aplicacion de algortimo de ordenamiento burbuja
print("Ordenamiento de una lista de números")

list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: ")) # Se pide al usuario que ingrese los elementos de la lista
    list.append(val)

while swapped:
    swapped = False
    for i in range(len(list) - 1): # Se recorre la lista
        if list[i] > list[i + 1]: # Si el elemento actual es mayor que el siguiente elemento, entonces intercambiarlos
            swapped = True # Se establece la bandera a True para un futuro intercambio
            list[i], list[i + 1] = list[i + 1], list[i] # Se intercambian los elementos

print("\nOrdenada:")
print(list)