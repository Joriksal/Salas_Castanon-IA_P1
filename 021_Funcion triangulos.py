"""Practica No. 21
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

def es_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2

def formula_heron(lado1, lado2, lado3):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    return (semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3)) ** 0.5

def area_triangulo(lado1, lado2, lado3):
    if not es_triangulo(lado1, lado2, lado3):
        return None
    return formula_heron(lado1, lado2, lado3)

def menu():
    print("1. Verificar si es un triángulo")
    print("2. Calcular el área de un triángulo")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            lado1 = float(input("Introduce la longitud del primer lado: "))
            lado2 = float(input("Introduce la longitud del segundo lado: "))
            lado3 = float(input("Introduce la longitud del tercer lado: "))

            if es_triangulo(lado1, lado2, lado3):
                print("Es un triángulo válido.")
            else:
                print("No es un triángulo válido.")

        elif opcion == "2":
            lado1 = float(input("Introduce la longitud del primer lado: "))
            lado2 = float(input("Introduce la longitud del segundo lado: "))
            lado3 = float(input("Introduce la longitud del tercer lado: "))

            area = area_triangulo(lado1, lado2, lado3)
            if area is not None:
                print(f"El área del triángulo es: {area:.2f}")
            else:
                print("No es un triángulo válido, no se puede calcular el área.")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()