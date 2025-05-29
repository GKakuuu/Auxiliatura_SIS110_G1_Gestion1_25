# contador de ocurrencias con diccionarios

texto = "Hola mundo, hola Python, hola programación"

palabras = texto.lower().replace(",", "").split()  # Convertir a minúsculas, eliminar comas y dividir en palabras
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1  # Incrementar el contador si la palabra ya existe
    else:
        contador[palabra] = 1  # Inicializar el contador si la palabra no existe

# Imprimir el contador de ocurrencias
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")