"""Practica No. 17
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Parametros de una funcion
def message(number):
    print("Ingresa un número:", number)
 
message(1)

# Ejemplos de funcion con parametros

def message(what, number):
    print("Ingresa", what, "número", number)
 
message("teléfono", 11)
message("precio", 5) 
message("número", "número") 

# Ejemplo de funcion con argumentos posicionales

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Luke", "Skywalker") # Argumentos posicionales
introduction("Jesse", "Quick") # Argumentos posicionales
introduction("Clark", "Kent")  # Argumentos posicionales

# Paso de argumento de palabra clave

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond") # Argumentos de palabra clave
introduction(last_name = "Skywalker", first_name = "Luke") # Argumentos de palabra clave