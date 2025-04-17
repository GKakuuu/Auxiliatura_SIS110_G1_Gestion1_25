# Ejercicio 3:
# Escribir un programa que pida un número entero y
# muestre por pantalla el primer y el último dígito.

import math

num = int(input("Ingrese un numero: "))

if num < 0:
    num = num * -1

tam = int(math.log10(num)) + 1

last = int(num % 10)
first = int(num / (10 ** (tam - 1)))

print("El primer digito es: ", first)
print("El ultimo digito es: ", last)