"""Practica No. 1
    Nombre: José Ricardo Salas Castañón
    Registro: 22310269 
    Grupo 6E
    Materia: Inteligencia Artificial"""

# 1 - Las Diferentes formas de expresar print

print("¡Hola mundo!")   #Las formas funcionan
print('¡Hola mundo!')

# 2 - Caracteres de espae y nuevas lineas

print("La Witsi Witsi Araña\nsubió a su telaraña.") #El\n sirve para empezar una nueva linea, sin volver a escribir la funcion print
print()
print("Vino la lluvia\ny se la llevó.")

# 3 - Multiples Argumentos

print("Jose","Ricardo","Salas","Castañon") #En una sola linea podemos mas de un argumento, separados por una coma

# 4 - Argumentos posicionales

print("Mi nombre es","Jose.") #Por obvias razones se ejecutara por completa la primera linea con print y todos sus argumentos y despues el print de la siguiente linea
print("Jose Salas.")

# 5 - Argumentos de palabra clave

print("Mi nombre es", "Jose.", end=" ") #El argumento de plabara clave end determina los carcateres que la funcion print envia a la salida una vez que llega al final de sus argumentos
print("Jose Salas.")

print("Mi","nombre","es","Jose","Salas.",sep="_")  #Esta palabra hace que en cada espacio entre cada argumento que tiene print, utilice el caracter que se asgino para separar los argumentos

print("Mi","nombre","es", sep="-",end="+")
print("Jose","Salas.", sep="+", end="*\n")

print("Programming","Essentials","in",sep="***",end="...")
print("Python")

# Juego de la flecha con pocos print

print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")