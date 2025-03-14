"""Practica No. 19
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Alcance en funciones

def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

# Ahora con este siguiente fragmento de codigo, las variables se encuentran dentro de la funcion, por lo que no se puede acceder a ellas desde fuera de la funcion.

def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
 
 
var = 1
my_function()
print(var)

# Palabra clave global

def my_function():
    global var # Con la palabra clave global, se puede acceder a la variable desde fuera de la funcion
    var = 2 # Se le asigna un nuevo valor a la variable
    print("¿Conozco a aquella variable?", var)


var = 1 # Se le asigna un valor a la variable
my_function() # Se llama a la funcion
print(var)  # Se imprime el valor de la variable

# Interracion de la funcion con sus argumentos

def my_function(n):
    print("Yo recibí", n) # Se imprime el valor de n
    n += 1  # Se le suma 1 a n
    print("Ahora tengo", n) # Se imprime el nuevo valor de n


var = 1 # Se le asigna un valor a la variable
my_function(var) # Se llama a la funcion
print(var) 

# Otro ejemplo - En este dentro de la funcion no se puede modificar el argumento de la funcion 
# Por lo tanto los print saldran como si esa linea de my_list_1 no existiera

def my_function(my_list_1):
    print("Print #1:", my_list_1)  
    print("Print #2:", my_list_2) 
    my_list_1 = [0, 1] # Preste atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)



