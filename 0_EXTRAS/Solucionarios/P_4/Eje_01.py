# El resultado de una prueba es "OOXXOXXOOO". Una 'O' significa una respuesta correcta de un
# problema y una 'X' significa una respuesta incorrecta. La puntuación de cada problema de esta
# prueba se calcula por sí misma y sus 'O's consecutivos anteriores solo cuando la respuesta es
# correcta. Por ejemplo, la puntuación del décimo problema es el 3 que se obtiene por sí mismo y
# sus dos anteriores 'O's consecutivas.
# Por lo tanto, la puntuación de "OOXXOXXOOO" es 10, que se calcula mediante
# "1+2+0+0+1+0+0+1+2+3". Debe escribir un programa que calcule las puntuaciones de los
# resultados de las pruebas.
# Entrada
# La entrada consiste en T casos de prueba, el número de prueba casos T se da en la primera línea
# de la entrada. Cada caso de prueba comienza con una línea que contiene una cadena compuesta
# por 'O' y 'X' y la longitud de la cadena es mayor que 0 y menor que 80. No hay espacios entre 'O' y
# 'X'.
# Salida
# Imprima exactamente una línea para cada caso de prueba. La línea contiene la puntuación de cada
# caso de prueba.

# ENTRADA
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

# SALIDA
# 10
# 9
# 7
# 55
# 30

T = int(input())
for _ in range(T):
    answers = input().strip()
    score = 0
    consecutive = 0
    for c in answers:
        if c == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0
    print(score)
