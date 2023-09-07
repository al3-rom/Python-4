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

# Analizamos los datos
genero = peli[:,1]
lanzamiento = peli[:,3]
duracion = peli[:,2]



        





