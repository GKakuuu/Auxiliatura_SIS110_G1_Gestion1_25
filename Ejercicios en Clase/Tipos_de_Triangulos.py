T1 = float(input("Ingrese el lado 1 del triángulo: "))
T2 = float(input("Ingrese el lado 2 del triángulo: "))
T3 = float(input("Ingrese el lado 3 del triángulo: "))

if T1 == T2 == T3:
    print("El triángulo es equilátero")

elif T1 == T2 or T2 == T3 or T1 == T3:
    print("El triángulo es isósceles")

else:
    print("El triángulo es escaleno")