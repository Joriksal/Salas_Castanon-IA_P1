"""Practica No. 7
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - Operador "=="

# El operador "==" hace la funcion de comparar y da imprime si es True o False, compruebe con el siguiente lineas

print("==\n")

var = 4  # Asignando 4 a var
print(var == 4)

var = 7  # Asignando 7 a var
print(var == 10)

# El operador "!=", solo que a la inversa, si son iguales da False y si no lo son, da True

print("!=\n")

var = 20  # Asignando 20 a var
print(var != 20)
 
var = 3  # Asignando 3 a var
print(var != 0)

# El operador >, si un numero es mayor que otro

print(">\n")

var = 10  # Asignando 10 a var
print(var > 5) # Var es mayor a 5?
 
var = 3  # Asignando 4 a var
print(var > 8) # Var es mayor a 8?

"""Esto sirve para su operador inverso, osea < funciona igual, solo que comparas si el numero 
    es mas pequeño que otro"""

# Operador ">=" o "<=", compara si es mayor o menor que un numero, pero tambien se cumple la condicion si es igual el numero comparado

print(">= o <=\n")

var = 10  # Asignando 10 a var
print(var >= 10) # Var es mayor a 5?
 
var = 3  # Asignando 4 a var
print(var >= 8) # Var es mayor a 8?

# 2 - Condicion If-else
""" Si la condicion se cumple, se ejecuta un bloque de instrucciones especificas dentros del if
    si no se cumple, entonces se ejecuta el bloque de instrucciones dentro del else """

# Se leen dos números

print("If-else -> Cual es el numero mayor? \n")

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if numero1 > numero2:
    numero_mayor = numero1
else:
    numero_mayor = numero2
 
# Imprime el resultado
print("El número más grande es:", numero_mayor)

# Tambien se pueden usar la funcion max() y min()

print("max() -> Cual es el numero mayor? \n")

# Se leen tres números.
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
 
numero_mayor = max(numero1, numero2, numero3)
 
# Imprime el resultado.
print("El número más grande es:", numero_mayor)

print("min() -> Cual es el numero mayor? \n")

# Se leen tres números.
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))
 
numero_menor = min(numero1, numero2, numero3)
 
# Imprime el resultado.
print("El número mas pequeño es:", numero_menor)
