"""Practica No. 26
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Cuando los datos no son lo que deberían ser
def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Tipo de dato no válido.")
    else:
        print(f"El resultado de la división es: {resultado}")
    finally:
        print("Fin del bloque try-except.")

# La rama try-except
# La excepción confirma la regla
# Cómo lidiar con más de una excepción
def manejar_excepciones():
    try:
        # Intentamos abrir un archivo que no existe
        with open('archivo_inexistente.txt', 'r') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# La excepción predeterminada y cómo usarla
def excepcion_predeterminada():
    try:
        # Intentamos convertir una cadena no numérica a entero
        numero = int("no es un número")
    except:
        print("Error: No se pudo convertir la cadena a entero.")

# Algunas excepciones útiles
def excepciones_utiles():
    try:
        lista = [1, 2, 3]
        print(lista[5])
    except IndexError:
        print("Error: Índice fuera de rango.")

# Por qué no puedes evitar probar tu código
# Pruebas, pruebas y más pruebas
import unittest

class PruebasUnitarias(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(1 + 1, 2)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            resultado = 1 / 0

# print debugging (depuración)
def depuracion_con_print():
    valor = 10
    print(f"El valor inicial es: {valor}")
    valor += 5
    print(f"El valor después de sumar 5 es: {valor}")

# Algunos consejos útiles
def consejos_utiles():
    # Usar comentarios para explicar el código
    # Mantener el código simple y legible
    # Usar nombres descriptivos para variables y funciones
    pass

# Pruebas unitarias – un mayor nivel de codificación
if __name__ == "__main__":
    # Ejecutar pruebas unitarias
    unittest.main()

    # Ejemplos de uso
    dividir(10, 2)
    dividir(10, 0)
    dividir(10, 'a')
    manejar_excepciones()
    excepcion_predeterminada()
    excepciones_utiles()
    depuracion_con_print()