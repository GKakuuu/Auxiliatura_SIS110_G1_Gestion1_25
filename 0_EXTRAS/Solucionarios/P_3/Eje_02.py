# Ejercicio 2: El oráculo de los números

# En un templo perdido, los monjes consultan un oráculo numérico que clasifica a los visitantes según su
# “número de alma”. Este número se obtiene al sumar los dígitos de un número dado repetidamente hasta que
# solo quede un dígito (ej. 9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2).
# Tu misión es construir un sistema que reciba varios números (uno por línea) y retorne el número de alma de cada
# uno.

# Entrada:
# 132189

# Salida:
# 6

def numero_de_alma(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


linea = input()
n = int(linea.strip())

print(numero_de_alma(n))
