# Un pirata ha escondido su tesoro en una secuencia de N números positivos.
# Para encontrar el número mágico que indica la posición del cofre, debes
# contar cuántos números consecutivos (empezando desde el primero) se deben
# sumar hasta alcanzar o superar un número objetivo T. 

# Entrada: 
# • Un entero N (1 ≤ N ≤ 1000) 
# • Una lista de N números positivos 
# • Un número objetivo T (1 ≤ T ≤ 10⁵) 
# Salida: 
# • Imprime cuántos números consecutivos se necesitaron para alcanzar o superar T. 
# • Si nunca se alcanza, imprime "Tesoro perdido". 

N = int(input("Ingrese el número de elementos: "))

numeros = list(map(int, input("Ingrese los números separados por espacio: ").split()))

T = int(input("Ingrese el número objetivo T: "))

if sum(numeros) < T:
    print("Tesoro perdido")

else:        
    suma = 0
    contador = 0
    for numero in numeros:
        suma += numero
        contador += 1
        if suma >= T:
            print(f"Números necesarios: {contador}")
            break