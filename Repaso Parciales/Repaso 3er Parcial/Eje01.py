# definir 4 operaciones con funciones y estas mismas llamarlas
# dentro de una funcion menu

def suma(a, b):
    """Suma dos números."""
    return a + b
def resta(a, b):
    """Resta dos números."""
    return a - b
def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b
def division(a, b):
    """Divide dos números."""
    if b == 0:
        return "Error: División por cero"
    return a / b

def menu():
    """Muestra un menú de operaciones y ejecuta la operación seleccionada."""
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Ingrese el número de la operación: ")
    
    if opcion in ['1', '2', '3', '4']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            resultado = suma(a, b)
        elif opcion == '2':
            resultado = resta(a, b)
        elif opcion == '3':
            resultado = multiplicacion(a, b)
        elif opcion == '4':
            resultado = division(a, b)
        
        print(f"El resultado es: {resultado}")
    else:
        print("Opción no válida.")

# Llamar a la función menu para ejecutar el programa
while True:
    menu()
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break

