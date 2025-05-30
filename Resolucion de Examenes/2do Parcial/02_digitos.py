# leer un entero n y mostrar por pantalla la cantidad de
# digitos 1-9 que existen entre 1 y n. (1 <= n <= 10^12)

n = int(input())

digitos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for i in range(1, n + 1):
    for digito in str(i):
        if digito != '0':
            digitos[int(digito)] += 1

for i, count in digitos.items():
    print(f"{i}: {count}")