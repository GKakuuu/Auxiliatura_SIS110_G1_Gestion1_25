# Ejercicio 8: El sistema de evaluación de Helix Corp
# La empresa Helix Corp evalúa a sus empleados según un esquema complejo. Cada empleado tiene:
# • Un nombre.
# • Un historial de evaluaciones (una lista de números del 1 al 10).
# • Cada evaluación tiene un peso, que depende de la posición en la lista: las más recientes valen más.
# La fórmula para calcular la evaluación final es:

# eval_final = sum(nota_i * peso_i) / sum(pesos)

# Donde: peso_i = i + 1
# Implementa una función que reciba un diccionario con los empleados y devuelva el nombre del mejor evaluado.

# Entrada:
# {
# "Lucía": [7, 8, 9],
# "Marco": [10, 6, 7],
# "Renzo": [8, 8, 8]
# }

# Salida:
# Mejor evaluado: Lucía (nota final: 8.33)

def mejor_evaluado(empleados):
    def eval_final(notas):
        pesos = [i + 1 for i in range(len(notas))]
        return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
    
    mejor = None
    mejor_nota = float('-inf')
    for nombre, notas in empleados.items():
        nota = eval_final(notas)
        if nota > mejor_nota:
            mejor_nota = nota
            mejor = nombre
    return f"Mejor evaluado: {mejor} (nota final: {mejor_nota:.2f})"

# Ejemplo de uso:
empleados = {
    "Lucía": [7, 8, 9],
    "Marco": [10, 6, 7],
    "Renzo": [8, 8, 8]
}
print(mejor_evaluado(empleados))
