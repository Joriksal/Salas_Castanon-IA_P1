"""Practica No. 23
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Función para calcular el número Fibonacci en la posición n

def fibonacci(n):
    # Si el número es menor que 1, no es válido para la secuencia Fibonacci
    if n < 1:
        return None
    # Los primeros dos números de Fibonacci son 1
    if n < 3:
        return 1

    # Inicializamos los dos primeros elementos de la secuencia
    elem_anterior_1 = elem_anterior_2 = 1
    suma = 0

    # Calculamos el número Fibonacci iterativamente
    for i in range(3, n + 1):
        suma = elem_anterior_1 + elem_anterior_2
        # Actualizamos los valores de los elementos anteriores
        elem_anterior_1, elem_anterior_2 = elem_anterior_2, suma

    return suma

# Función para mostrar el menú y obtener la opción del usuario
def menu():
    print("1. Calcular el número Fibonacci")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función principal que controla el flujo del programa
def main():
    while True:
        # Mostrar el menú y obtener la opción del usuario
        opcion = menu()

        # Opción 1: Calcular el número Fibonacci
        if opcion == "1":
            try:
                # Pedir al usuario que ingrese un número entero positivo
                numero = int(input("Introduce un número entero positivo: "))
                # Verificar que el número sea positivo
                if numero < 1:
                    print("El número debe ser positivo.")
                else:
                    # Calcular el número Fibonacci en la posición dada
                    resultado = fibonacci(numero)
                    # Mostrar el resultado al usuario
                    print(f"El número Fibonacci en la posición {numero} es: {resultado}")
            except ValueError:
                # Manejar errores si el usuario no ingresa un número válido
                print("Entrada no válida. Introduce un número entero.")

        # Opción 2: Salir del programa
        elif opcion == "2":
            print("Saliendo del programa...")
            break  # Terminar el bucle y salir del programa

        # Opción no válida: Pedir al usuario que ingrese una opción válida
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()