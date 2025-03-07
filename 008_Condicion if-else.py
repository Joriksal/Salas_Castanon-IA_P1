"""Practica No. 8
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Aplicaciones de la condicion if-else

print("Taxis e impuestos")

# Si los ingresos es menor a 50k pesos, se paga el 18 % y mas 500 pesos

ingresos = float(input("Introduce el ingreso anual: "))

if ingresos < 50000:
	imp = ingresos * 0.18 + 500
else:   # Si es mayor a 50000 se paga el 32 % mas 15k pesos
	imp = (ingresos - 50000) * 0.32 + 15000

if imp < 0.0:
	imp = 0.0

imp = round(imp, 0)
print("El impuesto es:", imp, "pesos")

# Aplicaciones de la condicion if-elif-else

print("\nIf-elif-else -> Si el año es bisiesto?")

año = int(input("Introduce un año: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if año % 4 != 0:
		print("Año Común")
	elif año % 100 != 0:
		print("Año Bisiesto")
	elif año % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
		
"""Estos son muy buenas aplicaciones para la condicion if-else y if-elif-else, en aplicaciones mas cotidianas
    y mas utiles y comprensibles"""
	
 