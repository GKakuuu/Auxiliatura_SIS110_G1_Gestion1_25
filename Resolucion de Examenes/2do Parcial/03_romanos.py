# leer 2 cadenas (a, b) que representan numeros romanos
# y mostrar por pantalla el resultado de la suma de ambos

romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

a = input("Ingrese el primer número romano: ").upper()
b = input("Ingrese el segundo número romano: ").upper()

# Convertir romano a entero
def romano_a_entero(s):
    total = 0
    prev = 0
    for c in reversed(s):
        valor = romanos[c]
        if valor < prev:
            total -= valor
        else:
            total += valor
        prev = valor
    return total

# Convertir entero a romano
def entero_a_romano(num):
    valores = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    resultado = ''
    for v, simbolo in valores.items():
        while num >= v:
            resultado += simbolo
            num -= v
    return resultado

entero_a = romano_a_entero(a)
entero_b = romano_a_entero(b)
suma = entero_a + entero_b
print(entero_a_romano(suma))