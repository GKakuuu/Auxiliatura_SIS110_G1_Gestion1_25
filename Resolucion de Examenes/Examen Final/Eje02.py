from collections import deque

# 2.	Un robot desea salir de una habitación vacía por una puerta diferente
# por la cual ingreso, para lo cual tiene la información de las rutas, el
# necesita un programa para encontrar la cantidad mínima de cuadros que tiene
# que recorrer para poder salir del laberinto, el robot solo puede ir hacia 
# arriba, abajo, izquierda o derecha. La entrada de valores comienza con el
# tamaño del laberinto N que es una matriz de NxN, a continuación NxN valores
# de letras donde: * representa una casilla por la que se puede caminar, X que
# representa una pared, A que representa el inicio del laberinto, y B que representa
# la puerta de salida. El programa debe imprimir la cantidad mínima de cuadros que
# debe recorrer el robot para salir del laberinto asumiendo que su punto de partida
# es el punto A.
# Input
# 3
# XAX
# X*X
# XBX

# Output
# 2

n = int(input())

box = []
xA = 0
yA = 0

xB = 0
yB = 0

for i in range (n):
    aux = input().lower()   
    for j in aux:
        if j == 'a':
            xA = aux.index('a')
            yA = i + 1
        if j == 'b':
            xB = aux.index('b')
            yB = i + 1

print(xA, yA)
print(xB, yB)

print(abs(xA-xB) + abs(yA-yB))
