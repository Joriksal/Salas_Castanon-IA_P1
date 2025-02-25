"""Practica No. 2
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - Diferencia entre cadena y entero

print ("2")
print (2)      #Imprimen lo mismo, el primero es una cadena y el segundo es un numero entero

# 2 - Numeros octales y hexadecimales

print (0o123)   #Al imprimir se imprime su valor decimal (83) pero nosotros lo ponemos en octal

print (0x123)   #Al imprimir se imprime su valor decimal (83) pero nosotros lo ponemos en hexadecimal

# 3 - Flotantes 

print (4.0) #El punto lo convierte en flotante

print (.4)  #El cero antes del punto se puede omitir por que es un numero flotante

# 4 - Enteros vs Flotantes

print (4)   #Este es un numero entero
print (4.0) #Este tambien es numero entero, pero para python es flotante por el punto.

#Tambien se puede usar notacion cientifica

print (3E8) #Este es un numero muy grande y es un flotante

print (3E-8)    #Este es un numero muy pequeño y por lo tanto es flotante

# 5 - Codificando flotante

print(0.0000000000000000000001) #Python puede usar notacion cientifica cuando sea necesario

# 6 - Cadenas

print ("Me gusta \"Monty Python\"") #Asi se hace para usar comillas dentro de otras comillas

print ('Me gusta "Monty Python"')   #Esta es la otra opcion sin necesidad de usar \ los de escape

# 7 - Codificando Cadenas

#Aqui se escribira una misma oracion en las dos formas posibles 

print('I\'m Jose Salas.')

print("I'm Jose Salas.")

# 8 - Valores Booleanos

print(True > False) #El resultado de esto, es True, ya que True es 1 y el False es 0, por lo tanto el 1 > 0 es 1 o True

print(True < False) #El resultado de esto, es False, ya que True es 1 y el False es 0, por lo tanto 1 < 0 es 0 o False

"""Se debe de escribir un fragmento de codigo de una sola linea"""

print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")