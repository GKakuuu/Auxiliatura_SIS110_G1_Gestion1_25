# Escribir una funcion para recibir una lista y determinar
# la cantidad de numeros primos que contiene.
# input             Output
# 7 5 9 11          3
# 0 1 2             1

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(lista):
    contador = 0
    for numero in lista:
        if es_primo(int(numero)):
            contador += 1
    return contador


entrada = input("Ingrese una lista de numeros separados por espacios: ")
lista_numeros = entrada.split()
print("Lista de numeros:", lista_numeros)
print("Cantidad de numeros primos:", contar_primos(lista_numeros))