"""Practica No. 10
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - Bucle for 

# Es un bucle parecido al while, colo que este esta mas diseñado para que se haga una determinada cantidad x de veces

# Este si es mas como un contador especifico, puedes establecer el rango cunatas veces quieres que se haga

# Contador de 0 a 9

print("Contador de 0 a 9\n")

for i in range(10):
    print("El valor de i es", i)

# Tambien se puede tener 2 argumentos en range

print("Contador de 2 a 7")

for i in range(2, 8):
    print("El valor de i es", i)

# Tambien se puede tener 3 argumentos en range
print("Range con 3 argumentos\n")

for i in range(2, 8, 3):
    print("El valor de i es", i)

# Aplicacion del bucle for, el cual es escribir las primeras potencias de dos
print ("Aplicacion de bucle For\n")

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

# Al for tambien se le puede añadir el else, para que al finalizar el bucle realice unas instrucciones
print ("Bucle For con else\n")

for i in range(5):
    print(i)
else:
    print("else:", i)

