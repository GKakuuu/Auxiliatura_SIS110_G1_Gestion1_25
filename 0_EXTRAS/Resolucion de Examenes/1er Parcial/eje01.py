# 1. Escribir un programa para leer dos numeros enteros y
# mostrar por pantalla la cantidad total de simbolos que existen:
# Ejemplo del caso 3:
# * ** * ** *
# * ** * ** *
# * ** * ** *

# Input     Output
# 1  1      1
# 1  5      7
# 3  5      21

num1 = int(input("Ingrese el primer número (filas): "))
num2 = int(input("Ingrese el segundo número (columnas): "))

# Calculamos la cantidad de columnas impares y pares
impares = (num2 + 1) // 2
pares = num2 // 2

print("Columnas impares:", impares)
print("Columnas pares:", pares)

# Calculamos el total de símbolos
total_simbolos = num1 * (impares * 1 + pares * 2)

# Mostramos el resultado
print("La cantidad total de símbolos es:", total_simbolos)