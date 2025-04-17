a = int(1)

while (a < 5) :
    print(a , "es menor a 5")
    a = a + 1

print("Fin del programa")


# crear un programa que sume todos los numeros
# introducidos por teclado, hasta que se introduzca
# el numero 0, cuando suceda esto, mostrar la suma

suma = 0

while True: # mientras no se encuentre algun break, no saldré del bucle
    aux = int(input())
    suma = suma + aux

    if aux == 0:
        break # rompe el primer bucle que encuentre

print("Suma: ", suma)

# Condiciones basicas
# ==    igual que
# !=    diferente de que
# <=    menor o igual que
# >=    mayor o igual que
# <     menor que
# >     mayor que
# True  mientras no se encuentre algun break, no saldré del bucle


# mostrar la cantidad de digitos que tiene un numero
# haciendo uso del bucle While

n = int(input())

dig = 0
div = 10

while n != 0:
    n = int(n / 10)
    dig = dig + 1

print (dig)