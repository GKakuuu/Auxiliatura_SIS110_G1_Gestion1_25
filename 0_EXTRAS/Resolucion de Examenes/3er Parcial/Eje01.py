# escribir una funcion para contar la cantidad de
# vocales mayusculas y minusculas en una cadena
# input         Output
# Hola          2
# Sistemas      3

def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in 'aeiou':
            contador += 1

        # if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
            # contador += 1
    return contador


entrada = input("Ingrese una cadena: ")
print("Resultado: ", contar_vocales(entrada))