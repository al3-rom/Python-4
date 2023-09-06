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