"""Practica No. 16
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Primera funcion - Lo que se ahorar con una funcion

print("Ingresa un valor: ")
a = int(input())

print("Ingresa un valor: ")
b = int(input())

print("Ingresa un valor: ")
c = int(input())

# Ahora lo haremos con una funcion

def message(): # Definicion de la funcion
    print("Ingresar valor: ") # Cuerpo de la funcion

print("Inicia aqui.")
message() # Llamada a la funcion
print("Termina aqui.")

# Aplicacion de la funcion
message() 
a = int(input()) 
message()
b = int(input())
message()
c = int(input())

"""En vez de llamar tres veces el print para pedir un valor, mejor llama tres veces a la funcion y listo"""
 