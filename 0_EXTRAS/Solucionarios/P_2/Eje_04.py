# Secuencias de Divisores 

N = int(input())


for _ in range(N):
    n = int(input())

    suma = 1 if n > 1 else 0

    i = 2

    while i * i <= n: 
        if n % i == 0:
            suma += i
            if i != n // i and i != 1:
                suma += n // i
        i += 1

    resultado = []
    if suma == n:
        resultado.append("perfecto")

    if suma != n and suma > 0:
        suma2 = 1 if suma > 1 else 0
        j = 2

        while j * j <= suma:
            if suma % j == 0:
                suma2 += j
                if j != suma // j and j != 1:
                    suma2 += suma // j
            j += 1
        
        if suma2 == n:
            resultado.append("romántico")

    if suma > n:
        resultado.append("abundante")

    if not resultado:
        resultado.append("complicado")

    print(f"{n} {' '.join(resultado)}")
