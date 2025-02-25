"""Practica No. 4
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1- Ejemplo básico de declaración e impresión de una variable
var = 1
print(var)

# 2- Declaración de múltiples variables y su impresión
var = 1
account_balance = 1000.0  # Balance de la cuenta
client_name = 'Jose Salas'  # Nombre del cliente
print(var, account_balance, client_name)
print(var)

# 3- Uso de variables de tipo cadena
var = "3.8.5"  # Asignación de una cadena que indica la versión de Python
print("Python version: " + var)

# 4- Modificación de una variable y actualización de su valor
var = 1
print(var)
var = var + 1  # Incremento del valor de la variable
print(var)

# 5- Asignación de nuevos valores a una variable
var = 100
var = 200 + 300  # Asignación de un nuevo valor después de un cálculo
print(var)

# 6- Ejemplo de resolución de problemas matemáticos simples
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # Cálculo de la hipotenusa usando el teorema de Pitágoras
print("c =", c)

# 7- Ejemplo de uso de múltiples variables y operadores abreviados
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=',')

# 8- Suma de variables para encontrar el total
total_apples = john + mary + adam
print(total_apples)

# 9- Uso de operadores abreviados
x = 10
x *= 2  # Multiplicación abreviada
x += 1  # Incremento abreviado

# 10- Conversión de unidades usando operaciones matemáticas
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61  # Conversión de millas a kilómetros
kilometers_to_miles = kilometers / 1.61  # Conversión de kilómetros a millas
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

# 11- Evaluación de una expresión polinómica para diferentes valores de x
x = 0
x = float(x)  # Conversión de x a tipo flotante
y = 3 * x**3 - 2 * x**2 + 3 * x - 1  # Evaluación del polinomio
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)
