persona = { 
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

print("Datos de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")


del persona["profesion"]  # Eliminar la clave "profesion"

print("Datos de la persona:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# if "telefono" in persona:
#     print("La clave 'telefono' ya existe en el diccionario.")


# persona["ciudad"] = "Barcelona"  # Modificar el valor de la clave "ciudad"
# # Agregar una nueva clave-valor al diccionario
# persona["telefono"] = "123456789"

# if "telefono" in persona:
#     print("La clave 'telefono' se ha agregado al diccionario.")
