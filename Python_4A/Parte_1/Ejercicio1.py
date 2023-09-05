import numpy as np

# Crea un array_1 lleno ceros con una longitud de 8 elementos

 # array_1 = np.array([0] * 8)
# o
array_1 = np.zeros(8) 

print(array_1)
print("---------------")

# Haz que todos los elementos de este array sean igual a 2

array_1[:] = 2
print(array_1)
print("---------------")

# Crea un array_2 que contenga todos los números pares del 1 al 10.

#array_2 = np.array([2,4,6,8,10])

array_2 = np.arange(2,11,2) #( 2 al final es el salto) (2,4,6,8,10) 
print(array_2)
print("---------------")

# Suma todos los elementos del array_2 usando un bucle y después usando un método
# de numpy. Compara los resultados

suma_total = 0

# sumamos con un bucle
for num in array_2:
    suma_total += num
# el resultado
print("-------1--------")
print(suma_total)


# sumamos con un metodo de numpy

array_sum = np.sum(array_2)
print("--------2-------")
print(array_sum)
print("---------------")

# Revierte array_2 y guárdalo en una variable independiente. 

array_2_revertido = array_2[::-1] # usamos ::-1 para revertir
print(array_2_revertido)

print("---------------")

# Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y
# array_2_revertido
# (Pista: Investiga el uso de intersect1d() de numpy

# Encontramos los elementos comunes entre array_1 y array_2
comunes1 = np.intersect1d(array_1, array_2)
print("-------1--------")
print(comunes1)


# entre array_2 y array_2_revertido
comunes2 = np.intersect1d(array_2, array_2_revertido)
print("--------2-------")
print(comunes2)
print("---------------")

#Crea un arrays lleno de 1s con una longitud dada por el usuario
 
longitud = int(input("Ingrese la longitud del array: "))
array_unos = np.ones(longitud)
print(array_unos)









