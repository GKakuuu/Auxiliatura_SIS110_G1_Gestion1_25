# Ejercicio 3: Crónicas del templo de Arvak

# El templo de Arvak resguarda reliquias místicas divididas en cofres. Cada cofre contiene una lista de reliquias,
# y cada reliquia tiene un nivel de rareza del 1 al 100. Para evitar robos, las combinaciones que abren los cofres
# solo se activan si las reliquias dentro cumplen ciertos criterios:
# Criterios por cofre:
# • Al menos 3 reliquias deben tener un número primo como nivel.
# • La suma total debe ser divisible por 3 y 5.
# • No debe haber reliquias repetidas.
# Tu tarea es validar qué cofres pueden abrirse.

# Entrada:
# {
# "Cofre A": [13, 17, 19, 15, 30],
# "Cofre B": [2, 3, 5, 7, 13, 30],
# "Cofre C": [10, 20, 30, 40, 50]
# }

# Salida esperada:
# Cofres válidos: Cofre B

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def cofres_validos(cofres):
    validos = []
    for nombre, reliquias in cofres.items():
        # Al menos 3 reliquias con nivel primo
        primos = [r for r in reliquias if es_primo(r)]
        if len(primos) < 3:
            continue
        # Suma divisible por 3 y 5
        suma = sum(reliquias)
        if suma % 3 != 0 or suma % 5 != 0:
            continue
        # No debe haber reliquias repetidas
        if len(set(reliquias)) != len(reliquias):
            continue
        validos.append(nombre)
    return validos

cofres = {
    "Cofre A": [13, 17, 19, 15, 30],
    "Cofre B": [2, 3, 5, 7, 13, 30],
    "Cofre C": [10, 20, 30, 40, 50]
}

resultado = cofres_validos(cofres)
print("Cofres válidos:", ", ".join(resultado))