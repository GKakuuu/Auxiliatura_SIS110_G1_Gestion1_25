# Ejercicio 5: El códice de los nombres olvidados

# Un antiguo códice contiene registros de nombres de guerreros legendarios. Sin embargo, muchos de ellos
# aparecen en diferentes formas (mayúsculas, minúsculas, con espacios o duplicados).
# Tu tarea es procesar una lista de nombres y devolver:
# • Cuántos guerreros únicos hay (sin importar mayúsculas/minúsculas)
# • Cuál fue el nombre más común (considerando todas las formas que representan el mismo nombre)
# Usa un diccionario para contar la frecuencia de los nombres (normalizados a minúsculas y sin espacios).

# Entrada:
# ["Ares", "ares", "ThOr", "thor", " thor", "ARES", "Zeus"]

# Salida:
# Guerreros únicos: 3
# Nombre más común: Ares

def procesar_nombres(lista_nombres):
    frecuencia = {}
    nombre_original = {}
    for nombre in lista_nombres:
        normalizado = nombre.strip().lower()
        frecuencia[normalizado] = frecuencia.get(normalizado, 0) + 1
        # Guardar la primera aparición con formato original
        if normalizado not in nombre_original:
            nombre_original[normalizado] = nombre.strip().capitalize()
    # Cantidad de guerreros únicos
    guerreros_unicos = len(frecuencia)
    # Encontrar el nombre más común
    nombre_mas_comun = max(frecuencia, key=frecuencia.get)
    print(f"Guerreros únicos: {guerreros_unicos}")
    print(f"Nombre más común: {nombre_original[nombre_mas_comun]}")

# Ejemplo de uso:
nombres = ["Ares", "ares", "ThOr", "thor", " thor", "ARES", "Zeus"]
procesar_nombres(nombres)
