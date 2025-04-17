# Ejercicio 1:
# Escribir un programa que pida un número entero y
# muestre por pantalla la cantidad de dígitos que tiene.

num = int(input("Ingrese un numero: "))

if num < 0:
    num = num * -1

siznum = len(str(num))

print("El numero tiene ", siznum, " digitos")
