# Ejercicio 9: El mercado de Harnak

# En Harnak, una ciudad mercante, los precios de los productos cambian cada día. Los comerciantes llevan
# registros en un formato como:
# productos = {
# "manzanas": [2, 2, 2.5, 3, 2.8],
# "plátanos": [1, 1.2, 1.5, 1.4, 1.1],
# "peras": [2.5, 2.4, 2.6, 2.3, 2.2]
# }
# Tu misión es implementar una función que reciba este diccionario y devuelva el nombre del producto con menor
# variación (es decir, el que tuvo menor diferencia entre su precio más alto y más bajo).
# Usa funciones para calcular la variación de cada producto.

# Salida esperada:
# El producto más estable fue: peras

def variacion(precios):
    return max(precios) - min(precios)

def producto_mas_estable(productos):
    menor_var = None
    producto_estable = ""
    for producto, precios in productos.items():
        var = variacion(precios)
        if menor_var is None or var < menor_var:
            menor_var = var
            producto_estable = producto
    return producto_estable

# Ejemplo de uso
productos = {
    "manzanas": [2, 2, 2.5, 3, 2.8],
    "plátanos": [1, 1.2, 1.5, 1.4, 1.1],
    "peras": [2.5, 2.4, 2.6, 2.3, 2.2]
}

print("El producto más estable fue:", producto_mas_estable(productos))
