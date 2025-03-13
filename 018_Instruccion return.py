"""Practica No. 18
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Return sin expresion

def happy_new_year(wishes = True): # Funcion para desear un feliz año nuevo
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return # Aqui se termina
 
    print("¡Feliz año nuevo!")

happy_new_year()

# Return con expresion

def boring_function(): # Funcion aburrida
    return 123
 
x = boring_function()
 
print("La función boring_function ha devuelto su resultado. Es:", x)

# Efectos y resultados: listas y funciones

def list_sum(lst): # Funcion que suma los elementos de una lista
    s = 0
 
    for elem in lst:
        s += elem
 
    return s

print(list_sum([5, 4, 3]))

# Lista el resultado de la funcion

def strange_list_fun(n): # Funcion que regresa una lista
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

# Ejercicio Un año Bisiesto

def is_year_leap(year): # Funcion para saber si un año es bisiesto
    if year % 4 != 0: # Si el año no es divisible entre 4
        return False
    elif year % 100 != 0: # Si el año no es divisible entre 100
        return True
    elif year % 400 != 0: # Si el año no es divisible entre 400
        return False # Si el año no es divisible entre 400
    else:
        return True # Si el año es divisible entre 400

test_data = [1900, 2023, 2016, 1987] # Datos de prueba
test_results = [False, True, True, False] # Resultados de prueba
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

