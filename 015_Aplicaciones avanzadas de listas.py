"""Practica No. 15
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# Compresion de listas

print("Ejemplo 1: Cuadrados de los números del 0 al 9")
squares = [x ** 2 for x in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print("Ejemplo 2: Números pares del 0 al 16")
twos = [2 ** i for i in range(8)] # [1, 2, 4, 8, 16, 32, 64, 128]

print("Ejemplo 3: Números impares del 0 al 10")
odds = [x for x in squares if x % 2 != 0 ]  # [1, 9, 25, 49, 81]

# Arreglos de dos dimensiones - Ajedrez 

EMPTY = 0 # Casilla vacía
ROOK = 1 # Torre
KNIGHT = 2 # Caballo
PAWN = 3 # Peón

board = [] # Tablero de ajedrez
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board = [[EMPTY for i in range(8)] for j in range(8)]  # Tablero de ajedrez

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][2] = KNIGHT

board[3][4] = PAWN

# Función para imprimir el tablero

def print_board(board):
    pieces = {EMPTY: '.', ROOK: 'R', KNIGHT: 'K', PAWN: 'P'}
    for row in board:
        print(" ".join(pieces[piece] for piece in row))

print_board(board)



