# escribir una funcion que reciba tres palabras y mostrar
# por pantalla las palabras sin vocales
# input             Output
# ing de sistemas   ng
#                   d
#                   sstms

def eliminar_vocales(palabras):
    resultado = ""
    for palabra in palabras:
        for letra in palabra:
            if letra.lower() not in 'aeiou':
                resultado += letra
        resultado += "\n"
    return resultado

palabras = input("Ingrese tres palabras separadas por espacios: ").split()
print(eliminar_vocales(palabras))