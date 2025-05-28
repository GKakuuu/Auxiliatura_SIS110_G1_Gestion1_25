# Ejercicio 2:
# Crear un programa que pida un número entero y muestre la
# primera mitad de ese número.
# Dicho numero siempre tendra una cantidad par de digitos.

num = int(input("Ingrese un numero: "))

split_num = str(num) [:len(str(num)) // 2]

print("La mitad del numero es: ", split_num)
