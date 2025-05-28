# Ejercicio 3:
# Escribir un programa que pida un número entero y
# muestre por pantalla el primer y el último dígito.

num = int(input("Ingrese un número: "))

siznum = len(str(num))

print("El primer dígito es: ", str(num)[0])
print("El último dígito es: ", str(num)[siznum-1])