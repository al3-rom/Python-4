"""
Supongamos que tienes un conjunto de datos de películas que contiene información
sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar
estos datos para determinar cuál es el género de película más popular, cuántas películas
se lanzaron en cada década y cuál es la duración promedio de cada género de película.


(Pista 1: puede ser util investigar np.unique, np.argsort y np.count_nonzero)
"""
# Importamos numpy
import numpy as np

# Creamos el array con pelis
peli = np.array([
    ["Anaconda", "Horror", 60, 2003, 9],
    ["KingKong", "Accion", 120, 1993, 5],
    ["KungfuPanda", "Comedia", 80, 2015, 8],
    ["DoctorStrange", "Comedia", 90, 2022, 10],
])

# Genero mas popular 

# return_counts sirve para contar cuantas veces aparece elemento
generos, conteos = np.unique(peli[:,1], return_counts = True)

# Ordenamos los conteos de mayor a menor
conteos_desc = np.argsort(conteos) [::-1] # nos devuelve los indices de los elementos del array conteos de mayor a menor
                                            # el resultado es [1,2,0]

# extraer el genero mas popular
genero_popular = generos[conteos_desc[0]] # conteos_desc[0] contiene el indice con el conteo mas alto
print("El genero mas popular es:", genero_popular)

# Agrupamos las peliculas por decada
# Creamos array con las dec adas a tratar
decadas = np.unique(peli[:,3].astype(int) // 10 * 10)
print(decadas)

# Contamos las peliculas en cada decada

conteos_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peli[:,3].astype(int) >= decada) & (peli[:,3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)
    print("En la decada de ", decada, "se crearon", conteo, "peliculas")

# Duracion promedio por genero

todos_generos = peli[:,1]
duraciones = peli[:,2]

duracion_media = np.zeros(len(generos))

for i in range(len(generos)):
                                                                                                                                         
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float))
    print("Duracion media de las peliculas de tipo: ", generos[i], "es de", duracion_media[i], "minutos")


        





