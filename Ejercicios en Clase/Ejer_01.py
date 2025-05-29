frase = input("Introduce una frase: ")

vocales = "aeiouAEIOU"

for letra in frase: # recorrer la frase letra por letra
    if letra in vocales:
        print(letra, end=" ")
