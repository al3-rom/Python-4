# Crea un arrays lleno de 1s con una longitud dada por el usuario
import numpy as np

# Creamos variable para poder crear array con el dato introducido por el usuario
longitud = int(input("Introduzca la longitud de array: "))

# Creamos el array
array1 = np.ones(longitud)

print(array1)

# Cambia la forma del array para que tenga una estructura de tipo (filas, columnas)

# Pediendo al usuario la nueva forma del array
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Comprobamos que el reshape es posible
if filas * columnas == longitud:
    # Realizamos el reshape
    nuevo_array = np.reshape(array1, (filas, columnas))
    print("Array con nueva forma: \n", nuevo_array )
else:
    # Indicamos que el reshape no es posible
    print("La cantidad de filas y columnas no es compatible con la longitud del array!")


# Crea una “matriz identidad” con la misma forma que el array anterior (filas, columnas)

matriz_identidad = np.eye(filas,columnas)
print("Matriz identiddad: \n", matriz_identidad)


# .Concatena ambas estructuras horizontalmente y verticalmente
# (Pista: Investiga el funcionamiento de concatenate() y de vstack() y hstack() de numpy)

# Concatenar horizontalmente

print("______________")
concat_horizont = np.concatenate((nuevo_array, matriz_identidad), axis = 1)
print(concat_horizont)

# Concatenar verticalmente 
print("______________")
concat_vert = np.concatenate((nuevo_array, matriz_identidad), axis = 0)
print(concat_vert)