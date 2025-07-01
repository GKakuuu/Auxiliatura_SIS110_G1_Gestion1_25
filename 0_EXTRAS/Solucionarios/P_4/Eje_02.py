

# En el juego Borderlands, los jugadores pueden encontrar y recolectar un variado conjunto de armas
# y equipo. Diseña un programa en Python que simule un sistema de botín para un jugador.
# Considera las siguientes condiciones:
# • Cada vez que el jugador derrota a un enemigo, tiene la oportunidad de encontrar botín.
# • El botín puede ser un arma, un escudo o un modificador de habilidad. Cada tipo de botín tiene
# un nivel de rareza: Común, Poco Común, Raro, Épico y Legendario.
# • Las armas tienen un nivel de daño, los escudos tienen una capacidad de absorción y los
# modificadores de habilidad mejoran alguna estadística específica del personaje.
# • Crea una función llamada `generar_botin` que simule el proceso de obtener botín. La función
# debe devolver un diccionario con la siguiente estructura:

# {
# 'tipo': 'Arma',        # Puede ser 'Arma', 'Escudo' o 'Modificador'
# 'rareza': 'Épico',     # Puede ser 'Común', 'Poco Común', 'Raro', 'Épico' o 'Legendario'
# 'atributo_1': valor_1, # Atributo específico del botín (por ejemplo, daño para armas)
# 'atributo_2': valor_2, # Atributo adicional (puede ser capacidad de absorción para escudos)
# 'atributo_3': valor_3  # Otro atributo adicional (por ejemplo, mejora de habilidad para modificadores)
# }


# • Después de obtener el botín, el programa debe imprimir un mensaje indicando el tipo, rareza
# y atributos del botín encontrado (Deje volar su imaginación todo lo que pueda!!!).
# • Preguntar al jugador si desea seguir enfrentándose a enemigos para obtener más botín. Si
# decide no continuar, muestra un resumen del botín obtenido durante la sesión.

# Consejo: Para poder generar de mejor forma un botín aleatorio utilizar la librería “random”

import random

TIPOS = ['Arma', 'Escudo', 'Modificador']
RAREZAS = ['Común', 'Poco Común', 'Raro', 'Épico', 'Legendario']

def generar_botin():
    tipo = random.choice(TIPOS)
    rareza = random.choices(RAREZAS, weights=[40, 30, 15, 10, 5])[0]
    botin = {'tipo': tipo, 'rareza': rareza}

    if tipo == 'Arma':
        daño = random.randint(10, 100) * (RAREZAS.index(rareza) + 1)
        velocidad = round(random.uniform(0.5, 2.5), 2)
        critico = random.randint(1, 20) * (RAREZAS.index(rareza) + 1)
        botin.update({'Daño': daño, 'Velocidad': velocidad, 'Crítico': critico})
    elif tipo == 'Escudo':
        absorcion = random.randint(50, 300) * (RAREZAS.index(rareza) + 1)
        recarga = round(random.uniform(1.0, 5.0), 2)
        resistencia = random.choice(['Fuego', 'Hielo', 'Corrosivo', 'Eléctrico', 'Ninguna'])
        botin.update({'Absorción': absorcion, 'Recarga': recarga, 'Resistencia': resistencia})
    else:  # Modificador
        stat = random.choice(['Salud', 'Velocidad', 'Daño', 'Recarga'])
        mejora = random.randint(5, 30) * (RAREZAS.index(rareza) + 1)
        duracion = random.randint(10, 60)
        botin.update({'Estadística': stat, 'Mejora': mejora, 'Duración': duracion})

    return botin

def mostrar_botin(botin):
    print(f"\n¡Has encontrado un botín {botin['rareza']} de tipo {botin['tipo']}!")
    for k, v in botin.items():
        if k not in ['tipo', 'rareza']:
            print(f"  {k}: {v}")

def resumen_botin(lista_botin):
    print("\nResumen de botín obtenido:")
    for i, botin in enumerate(lista_botin, 1):
        print(f"\nBotín #{i}:")
        print(f"  Tipo: {botin['tipo']}")
        print(f"  Rareza: {botin['rareza']}")
        for k, v in botin.items():
            if k not in ['tipo', 'rareza']:
                print(f"    {k}: {v}")

def main():
    botines = []
    while True:
        botin = generar_botin()
        mostrar_botin(botin)
        botines.append(botin)
        seguir = input("\n¿Quieres enfrentarte a otro enemigo? (s/n): ").strip().lower()
        if seguir != 's':
            break
    resumen_botin(botines)

if __name__ == "__main__":
    main()
