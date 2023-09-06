"""
ANALISIS DE DATOS - VENTAS POR MES
Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año.
Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la
venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos,
etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en
cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3
columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de
NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes.
(Pista 1) Tu array de entrada puede tener un a forma de este tipo:

ventas = np.array([
    ['2022-01-01', 100, 'ropa'],
    ['2022-01-02', 200, 'alimentacion'],
    ['2022-01-03', 150, 'ropa']

(Pista 2: puedes cambiar el tipo de dato del array de string a entero usando
array[:,i].astype(int) )
])
"""