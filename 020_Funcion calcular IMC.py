"""Practica No. 20
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Ejemplo calcular IMC - Funcion

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
    peso < 20 or peso > 200:
        return None

    return peso / altura ** 2

print(imc(80, 1.75))
def pies_pulgadas_a_metros(pies, pulgadas):
    return pies * 0.3048 + pulgadas * 0.0254

def libras_a_kg(libras):
    return libras * 0.453592

def main():
    print("Seleccione la opción de entrada de datos:")
    print("1. Metros y Kilogramos")
    print("2. Pies, Pulgadas y Libras")
    opcion = int(input("Opción: "))

    if opcion == 1:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))
    elif opcion == 2:
        pies = float(input("Ingrese su altura en pies: "))
        pulgadas = float(input("Ingrese su altura en pulgadas: "))
        peso_libras = float(input("Ingrese su peso en libras: "))
        altura = pies_pulgadas_a_metros(pies, pulgadas)
        peso = libras_a_kg(peso_libras)
    else:
        print("Opción no válida")
        return

    resultado = imc(peso, altura)
    if resultado:
        print(f"Su IMC es: {resultado:.2f}")
    else:
        print("Datos fuera de rango")

if __name__ == "__main__":
    main()