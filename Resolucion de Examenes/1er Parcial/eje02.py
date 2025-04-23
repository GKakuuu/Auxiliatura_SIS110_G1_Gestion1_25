# 2. Leer dos numeros enteros cuya cantidad de digitos
# siempre sera impar y formar un nuevo numero con los
# digitos del medio.

# Input             Output
# 173  76274        72
# 123  543          24
# 1    432          13

from math import log10

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

size1 = int(log10(num1) + 1) // 2
size2 = int(log10(num2) + 1) // 2

div1 = num1 // (10 ** size1)
div2 = num2 // (10 ** size2)

num3 = (div1 % 10) * 10 + div2 % 10

print(f"El nuevo numero es: {num3}")
