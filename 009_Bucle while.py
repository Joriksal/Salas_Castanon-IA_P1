"""Practica No. 9
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - El bucle while 

# Es una funcion, la cual hace que un conjunto de instrucciones se ejecute en un tiempo infinito dependiendo de una condicion

print("Almacena el actual número más grande aquí\n")

largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)

# Otro ejemplo es el de contadores como este:

print("Contador\n")

counter = 5 # Las veces que se imprimira la cadena de texto
while counter != 0:
    print("Dentro del bucle.", counter) # Cadena de texto a imprimir x numero de veces
    counter -= 1
print("\nFuera del bucle.", counter) # Ya que se termine el contador se imprime esta cadena cadena 

# 2 - Bucle while-else

""" Esta es la misma condicion, solo que al final tiene la funcion else, y es que al acabar el bucle o al no cumplir la condicion
    se ejecutara ese bloque de instrucciones"""


print("\nContador")

i = 1 # Iniccializa el contador en 1
while i < 5:
    print(i) # Imprime el numero que tiene el contador
    i += 1 # Se incrimente en 1 la variable de contador
else:
    print("else:", i) # Cuando ya no se cumpla la condicion de while ejecutara estas instrucciones del else

