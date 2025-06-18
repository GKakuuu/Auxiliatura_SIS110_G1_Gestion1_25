# Realizar un contador de digitos ocupando un bucle while 

def contador_digitos(numero):
    """Cuenta los dígitos de un número."""
    if numero < 0:
        numero = -numero  # Hacer el número positivo si es negativo
    contador = 0
    while numero > 0:
        numero //= 10  # Eliminar el último dígito
        contador += 1
    return contador


cantidad = int(input("Ingrese la cantidad de números a contar: "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    digitos = contador_digitos(numero)
    print(f"El número {numero} tiene {digitos} dígitos.")

