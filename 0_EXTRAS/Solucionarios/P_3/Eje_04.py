# Ejercicio 4: Cartas del torneo Runex

# En el juego Runex, los jugadores compiten con cartas mágicas. Cada carta tiene un nombre, tipo ("fuego",
# "agua" o "tierra") y un valor numérico.
# El poder de un jugador se calcula según las siguientes reglas:
# • Cada carta de fuego da su valor +2
# • Agua da su valor +1
# • Tierra da solo su valor
# • Si hay más de 3 cartas del mismo tipo, se suma un bonus de +5 al total

# Entrada ejemplo:
# [
# {"nombre": "Flamazo", "tipo": "fuego", "valor": 4},
# {"nombre": "Ola gigante", "tipo": "agua", "valor": 5},
# {"nombre": "Erosión", "tipo": "tierra", "valor": 6},
# {"nombre": "Piroexplosión", "tipo": "fuego", "valor": 7},
# {"nombre": "Fénix", "tipo": "fuego", "valor": 6}
# ]

# Salida esperada:
# Poder total del jugador: 35

def calcular_poder(cartas):
    poder = 0
    conteo_tipos = {"fuego": 0, "agua": 0, "tierra": 0}
    for carta in cartas:
        tipo = carta["tipo"]
        valor = carta["valor"]
        if tipo == "fuego":
            poder += valor + 2
        elif tipo == "agua":
            poder += valor + 1
        elif tipo == "tierra":
            poder += valor
        conteo_tipos[tipo] += 1
    if any(c > 3 for c in conteo_tipos.values()):
        poder += 5
    return poder

# Ejemplo de uso:
cartas = [
    {"nombre": "Flamazo", "tipo": "fuego", "valor": 4},
    {"nombre": "Ola gigante", "tipo": "agua", "valor": 5},
    {"nombre": "Erosión", "tipo": "tierra", "valor": 6},
    {"nombre": "Piroexplosión", "tipo": "fuego", "valor": 7},
    {"nombre": "Fénix", "tipo": "fuego", "valor": 6}
]

print("Poder total del jugador:", calcular_poder(cartas))
