"""
ANALISIS DE DATOS CLIMÁTICOS
Supongamos que tienes un conjunto de datos de clima que contiene información sobre la
temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres
analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál
fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para
ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde
n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los
datos por mes y calcular las medias de temperatura, humedad y presión atmosférica
correspondientes.
(Pista 1) Tu array de entrada podría ser algo como esto, con daros de temperatura,
humedad, presión y mes del año:

clima = np.array([
    [20,70,1009,1],
    [21,60,1011,1],
    [22,40,1010,2]
])

"""
import numpy as np


clima = np.array([
    [20,70,1009,1],
    [21,60,1011,1],
    [22,40,1010,2],
])

# Calcular la temperatura promedio por mes
meses = clima[:,3]
temperaturas = clima[:,0]
humedad = clima[:,1]
presion = clima[:,2]
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)
# Recorrer los valores para cada mes

for i in range(12):
    # Calculamos valores promedios
    temp_mes[i] = np.mean(temperaturas[meses == i+1])
    humedad_mes[i] = np.mean(humedad[meses == i+1])
    presion_mes[i] = np.mean(presion[meses == i+1])

    # Imprimimos resultados para cada mes
    print("La temperatura promedio en el mes", i+1, "fue de", temp_mes[i],"grados")
    print("La humedad promedio en el mes", i+1, "fue de", humedad_mes[i])
    print("La presion promedio en el mes", i+1, "fue de", presion_mes[i])
    