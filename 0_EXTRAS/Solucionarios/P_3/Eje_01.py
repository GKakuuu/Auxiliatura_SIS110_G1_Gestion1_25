# Ejercicio 1: Mensajes secretos del Archivo 6

# La agencia de inteligencia "Archivo 6" ha interceptado una serie de mensajes encriptados. Cada mensaje parece
# ser una combinación de palabras comunes, pero con un patrón curioso:
# Cada palabra ha sido invertida y los signos de puntuación han sido eliminados.
# Tu misión es construir un programa que lea una cadena de texto representando un mensaje interceptado, lo
# procese palabra por palabra, revierta cada una y devuelva el mensaje reconstruido con las palabras corregidas.

# Restricciones:
# • Solo se deben revertir palabras, no el orden total del mensaje.
# • Usa funciones para modular el proceso.

# Entrada ejemplo:
# soypitseD ed samohT zednem a otrebil nu

# Salida esperada:
# Destipyos de Thomas mendez a liberto un

import string

def limpiar_palabra(palabra):
    return ''.join(c for c in palabra if c not in string.punctuation)

def procesar_mensaje(mensaje):
    palabras = mensaje.split()
    palabras_revertidas = [limpiar_palabra(p)[::-1] for p in palabras]
    return ' '.join(palabras_revertidas)


mensaje = input("Ingrese el mensaje interceptado: ")
print(procesar_mensaje(mensaje))
