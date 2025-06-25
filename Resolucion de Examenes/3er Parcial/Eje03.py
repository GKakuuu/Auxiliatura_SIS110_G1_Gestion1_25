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
                resultado += letra + " "
        resultado += "\n"
    return resultado

# crear la misma funcion pero ocupando el metodo replace
def eliminar_vocales_replace(palabras):
    resultado = ""
    for palabra in palabras:
        sin_vocales = palabra.replace('a', ' ').replace('e', ' ').replace('i', ' ').replace('o', ' ').replace('u', ' ')
        # sin_vocales = sin_vocales.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
        resultado += sin_vocales + "\n"
    return resultado

palabras = input("Ingrese tres palabras separadas por espacios: ").lower().split()
print(eliminar_vocales(palabras))
print(eliminar_vocales_replace(palabras))
