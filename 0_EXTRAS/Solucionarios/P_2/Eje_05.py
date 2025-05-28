# En el reino de Pythonia, se lanzan palabras mágicas al azar.
# Por cada vocal encontrada en una palabra, el jugador suma puntos: 
# a = 1 pt, e = 2 pts, i = 3 pts, o= 4 pts, u = 5 pts 
# Calcula el total de puntos por cada palabra lanzada. 

# Entrada: 
# • Un entero N (1 ≤ N ≤ 50) 
# • N palabras (sin espacios) 
# Salida: 
# • Por cada palabra, imprime el puntaje obtenido.

N = int(input("Ingrese el número de palabras: "))
for _ in range(N):
    palabra = input("Ingrese una palabra: ")
    puntos = 0
    for letra in palabra.lower():
        if letra == 'a':
            puntos += 1
        elif letra == 'e':
            puntos += 2
        elif letra == 'i':
            puntos += 3
        elif letra == 'o':
            puntos += 4
        elif letra == 'u':
            puntos += 5
            
    print(f"{palabra}: {puntos}")