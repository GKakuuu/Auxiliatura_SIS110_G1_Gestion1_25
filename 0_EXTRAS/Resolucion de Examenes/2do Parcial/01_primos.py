# escribir un programa para leer dos numeros (a, b)
# y mostrar por pantalla la cantidad de numeros primos
# entre a y b (incluidos a y b).
# 1 <= a <= 1000000, a < b , 1 <= b <= 10^12

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())

contador = 0

for i in range(a, b + 1):
    if es_primo(i):
        contador += 1

print(contador)