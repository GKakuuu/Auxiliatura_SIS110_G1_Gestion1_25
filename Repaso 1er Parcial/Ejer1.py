# Ejercicio 1:
# Escribir un programa que pida un número entero y
# muestre por pantalla la cantidad de dígitos que tiene.

import math

num = int(input("Ingrese un numero: "))

if num < 0:
    num = num * -1

if num == 0:
    print("El numero tiene 1 digito")

else:
    siznum = int(math.log10(num)) + 1
    print("El numero tiene ", siznum, " digitos")