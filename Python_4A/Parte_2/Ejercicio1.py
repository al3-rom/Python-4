# Crea un array con 15 números enteros aleatorios entre 1 y 100
import numpy as np

#creamos array
array_1 = np.array([])
# sacamos 15 numeros aleatorios entre 1 y 100
array_1 = np.random.randint(1, 101, size = 15)
print("-------RANDOM(1-100)--------")
print(array_1)


# Multiplica todos los elementos del array usando un bucle y después usando un
# método de numpy. Compara los resultados

array_multiplicado1 = []
array_multiplicado2 = []

# Multiplicamos todos los elementos del array usando un bucle
for i in array_1:
    array_multiplicado1 = i*array_1
print("------1---------")
print(array_multiplicado1)

# usando numpy
array_multiplicado2 = np.dot(array_1, array_1)
print("------2---------")
print(array_multiplicado2)
print("---------------")

# Crea otro array con 15 números decimales aleatorios entre 0 y 1

array_2 = np.random.rand(15) 
print("---------------")
print(array_2)

# Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
# operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

# Sumamos con un operador
suma_operador = array_1 + array_2
print("-------1--------")
print(suma_operador)

# ahora con numpy
print("-------2--------")
suma_numpy = np.add(array_1,array_2)
print(suma_numpy)
print("---------------")

# Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

# Resolvemos usando el operador
restando_operador = array_1 - array_2
print("-------1--------")
print(restando_operador)

# usando numpy
print("-------2--------")
restando_numpy = np.subtract(array_1,array_2)
print(restando_numpy)
print("---------------")

# Haz lo mismo con la multiplicación elemento por elemento. Usa un operador y
# después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

multiplicacion_operador = array_1 * array_2
print("-------1--------")
print(multiplicacion_operador)

# usando numpy
print("-------2--------")
multiplicacion_numpy = np.multiply(array_1,array_2)
print(multiplicacion_numpy)


# Encuentra el valor más alto del primer array que has creado

mas_alto = np.max(array_1)
print("-------MAS ALTO--------")
print(mas_alto)

# Calcula la media (mean), la mediana (median) y al deviación estandar (standard
# deviation) de los arrays (Nota: No nos importa el significado matemático de estos
# valores, lo importante es que encuentres que función de numpy necesitas. Puedes
# hacer la búsqueda en castellano o en inglés, aunque en inglés muchas veces suele
# haber más resultados).

# calculamos la media

media = np.mean(array_1)
print("-------MEDIA--------")
print(media)

mediana = np.median(array_1)
print("-------MEDIANA--------")
print(mediana)

deviacion_estandar = np.std(array_1)
print("-------DEVIACION_MEDIA--------")
print(deviacion_estandar)