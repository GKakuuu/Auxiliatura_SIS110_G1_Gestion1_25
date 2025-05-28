# Ejercicio 2:
# Crear un programa que pida un número entero y muestre la
# primera mitad de ese número.
# Dicho numero siempre tendra una cantidad par de digitos.

import math

num = int(input("Ingrese un numero: "))

if num < 0: # Cambia el signo del numero
    num = num * -1

#calcula la cantidad de digitos del numero
tam = (int(math.log10(num)) + 1) / 2
split_num = int(num // (10 ** tam))

print("La mitad del numero es: ", split_num)