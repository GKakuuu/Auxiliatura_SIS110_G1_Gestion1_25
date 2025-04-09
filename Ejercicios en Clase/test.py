aux = int (input())

if aux > 0:
    print("es mayor a 0")
else:
    aux = aux * -1
    if (aux > 0):
        print("aux ahora si es mayor a 0")



aux = int (input())

if aux > 0:
    print("es mayor a 0")
elif (aux > 0):
    aux = aux * -1
    print("aux ahora si es mayor a 0")