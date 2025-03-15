"""Practica No. 25
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Definición de una tupla con cuatro elementos
mi_tupla = (1, 10, 100, 1000)

# Imprime el primer elemento de la tupla
print(mi_tupla[0])
# Imprime el último elemento de la tupla
print(mi_tupla[-1])
# Imprime todos los elementos de la tupla desde el segundo hasta el final
print(mi_tupla[1:])
# Imprime todos los elementos de la tupla excepto los dos últimos
print(mi_tupla[:-2])

# Itera sobre cada elemento de la tupla e imprime su valor
for elem in mi_tupla:
        print(elem)

# Diccionario

# Definición de un diccionario con traducciones de animales
diccionario = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# Definición de un diccionario con números de teléfono
numeros_telefono = {'jefe': 5551234567, 'Suzy': 22657854310}

# Definición de un diccionario vacío
diccionario_vacio = {}

# Imprime el diccionario de traducciones de animales
print(diccionario)

# Imprime el diccionario de números de teléfono
print(numeros_telefono)

# Imprime el diccionario vacío
print(diccionario_vacio)

# Metodos y funciones de los diccionarios

# Key()

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"} # Definición de un diccionario con traducciones de animales
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# Modificar, agregar y eliminar valores

# Modificar un valor

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"} # Definición de un diccionario con traducciones de animales
 
dictionary['gato'] = 'minou'
print(dictionary)

# La funcion sorted()

for key in sorted(dictionary.keys()): # sorted() ordena las claves del diccionario
      print(key, "->", dictionary[key])

# Agregar nuevas claves

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne' # Agrega una nueva clave
print(dictionary)

# Eliminar claves

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro'] # Elimina la clave 'perro'
print(dictionary)

# Ejemplo que utiliza tuplas y diccionarios

school_class = {}  # Diccionario vacío

while True:
    name = input("Ingresa el nombre del estudiante (deja en blanco para salir): ").strip()
    if name == '':  # Si el usuario deja el nombre vacío, sale del bucle
        break

    try:
        score = int(input("Ingresa la calificación del estudiante (0-10): "))
        if score not in range(0, 11):
            print("Error: La calificación debe estar entre 0 y 10.")
            continue  # Permite ingresar nuevamente
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue  # Evita que el programa crashe si se ingresa un valor no numérico

    if name in school_class:
        school_class[name] += (score,)  # Agrega la calificación a la tupla existente
    else:
        school_class[name] = (score,)  # Crea una nueva tupla con la calificación

# Calcular e imprimir el promedio de calificaciones por estudiante
if school_class:  # Solo imprime si hay datos registrados
    print("\nPromedios de calificaciones:")
    for name in sorted(school_class.keys()):  # sorted() ordena los nombres alfabéticamente
        adding = sum(school_class[name])  # Suma las calificaciones
        counter = len(school_class[name])  # Cuenta las calificaciones
        print(name, ":", round(adding / counter, 2))  # Imprime el promedio con 2 decimales
else:
    print("No se ingresaron calificaciones.")



    