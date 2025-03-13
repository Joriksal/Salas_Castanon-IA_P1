"""Practica No. 11
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Operadores logicos, funcionan mas o menos igual que las tablas de verdad que el algebra de Boole

# Operadores Lógicos
print("Operadores Lógicos:")

# AND lógico (and)
a = True
b = False
print(f"{a} and {b} = {a and b}")  # False

# OR lógico (or)
print(f"{a} or {b} = {a or b}")  # True

# NOT lógico (not)
print(f"not {a} = {not a}")  # False

# Operadores Bit a Bit
print("\nOperadores Bit a Bit:")    

# AND bit a bit (&)
x = 10  # 1010 en binario
y = 4   # 0100 en binario
print(f"{x} & {y} = {x & y}")  # 0 (0000 en binario)

# OR bit a bit (|)
print(f"{x} | {y} = {x | y}")  # 14 (1110 en binario)

# XOR bit a bit (^)
print(f"{x} ^ {y} = {x ^ y}")  # 14 (1110 en binario)

# NOT bit a bit (~)
print(f"~{x} = {~x}")  # -11 (en complemento a dos)

# Desplazamiento a la izquierda (<<)
print(f"{x} << 1 = {x << 1}")  # 20 (10100 en binario)

# Desplazamiento a la derecha (>>)
print(f"{x} >> 1 = {x >> 1}")  # 5 (0101 en binario)

# Explicación:
# Los operadores lógicos (and, or, not) se utilizan para combinar condiciones booleanas.
# Los operadores bit a bit (&, |, ^, ~, <<, >>) se utilizan para manipular bits individuales en números enteros.