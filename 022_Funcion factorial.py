"""Practica No. 22
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Ejemplo de función para calcular el factorial de un número

def factorial(numero):
    if numero < 0:
        return None
    if numero < 2:
        return 1

    producto = 1
    for i in range(2, numero + 1):
        producto *= i
    return producto

def menu():
    print("1. Calcular el factorial de un número")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            try:
                numero = int(input("Introduce un número entero no negativo: "))
                if numero < 0:
                    print("El número debe ser no negativo.")
                else:
                    resultado = factorial(numero)
                    print(f"El factorial de {numero} es: {resultado}")
            except ValueError:
                print("Entrada no válida. Introduce un número entero.")

        elif opcion == "2":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()