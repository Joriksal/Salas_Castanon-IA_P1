"""Practica No. 6
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - Funcion Input()

print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

# 2 - Conversion de tipos

anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

# 3 - Entradas y salidas simples

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")

# 4 - Operador y expresiones

x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

# 5 - Operadores y expresiones - 2

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # Calcula el número total de minutos
hour = hour + mins // 60 # Calcula el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # Corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # Corrige las horas para que estén en un rango de (0..23) 
print(hour, ":", mins, sep='')
