def operacion_externa(x):
    def operacion_interna(y):
        return y * 2
    resultado = operacion_interna(x) + 5
    return resultado

# Ejemplo de uso
print(operacion_externa(3))  # Salida: 11