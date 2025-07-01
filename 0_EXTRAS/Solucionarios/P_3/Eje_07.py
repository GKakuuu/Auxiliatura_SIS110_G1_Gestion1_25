# Ejercicio 7: La grieta del equilibrio

# En una simulación del mundo alterno de Tenebrax, existe un fenómeno natural llamado la grieta del equilibrio,
# que mide la armonía entre dos bandos: Los Luminares y Los Umbrales.
# Cada bando reporta una lista de eventos mágicos que afectan el equilibrio:
# • Los eventos son palabras.
# • Un evento “positivo” contiene más letras del alfabeto de la primera mitad (a-m),
# • Uno “negativo” contiene más letras de la segunda mitad (n-z).
# Tu tarea es:
# 1. Calcular el “puntaje” total para cada bando.
# 2. Indicar cuál bando está ganando o si hay equilibrio.

# Entrada:
# luminares = ["Luz", "Esencia", "Amar"]
# umbrales = ["Oscuridad", "Niebla", "Sombras"]

# Salida esperada:
# Luminares: 9
# Umbrales: 13
# Ganador: Umbrales

def puntaje_evento(evento):
    evento = evento.lower()
    mitad1 = set('abcdefghijklm')
    mitad2 = set('nopqrstuvwxyz')
    puntos = 0
    for letra in evento:
        if letra in mitad1:
            puntos += 1
        elif letra in mitad2:
            puntos += 2
    return puntos

def puntaje_total(lista_eventos):
    return sum(puntaje_evento(e) for e in lista_eventos)

luminares = ["Luz", "Esencia", "Amar"]
umbrales = ["Oscuridad", "Niebla", "Sombras"]

puntaje_luminares = puntaje_total(luminares)
puntaje_umbrales = puntaje_total(umbrales)

print(f"Luminares: {puntaje_luminares}")
print(f"Umbrales: {puntaje_umbrales}")

if puntaje_luminares > puntaje_umbrales:
    print("Ganador: Luminares")
elif puntaje_umbrales > puntaje_luminares:
    print("Ganador: Umbrales")
else:
    print("Equilibrio")
