# Ejercicio 6: El archivo de Mnemósine

# La biblioteca de la ciudad de Metrona está completamente automatizada y bajo el control de un sistema
# llamado Mnemósine. Este sistema es capaz de recordar cada libro prestado por cada usuario, pero un error
# reciente ha corrompido parcialmente los registros. Se te entrega una lista de registros incompletos donde cada
# entrada tiene el formato:
# "usuario: libro1, libro2, ..., libroN"
# Algunos registros están repetidos, otros tienen espacios irregulares o duplicados. Tu misión es reconstruir una
# versión limpia de los registros, asegurando:
# • Cada usuario solo aparece una vez.
# • Los títulos deben estar en orden alfabético y sin repeticiones.
# • El formato final debe ser: "usuario: libroA, libroB, libroC"

# Entrada:
# [
# "Ana: El Hobbit, Don Quijote ",
# "ana: el hobbit, Cien años de soledad",
# "Carlos: Fundación, 1984",
# "Carlos : 1984 , Fundación"
# ]

# Salida esperada:
# {
# "ana": "Cien años de soledad, Don Quijote, El Hobbit, el hobbit",
# "carlos": "1984, Fundación"
# }

def limpiar_registros(registros):
    usuarios = {}
    for registro in registros:
        if ':' not in registro:
            continue
        usuario, libros = registro.split(':', 1)
        usuario = usuario.strip().lower()
        libros_lista = [libro.strip() for libro in libros.split(',') if libro.strip()]
        if usuario not in usuarios:
            usuarios[usuario] = set()
        usuarios[usuario].update(libros_lista)
    resultado = {}
    for usuario, libros in usuarios.items():
        resultado[usuario] = ', '.join(sorted(libros))
    return resultado

# Ejemplo de uso:
registros = [
    "Ana: El Hobbit, Don Quijote ",
    "ana: el hobbit, Cien años de soledad",
    "Carlos: Fundación, 1984",
    "Carlos : 1984 , Fundación"
]
print(limpiar_registros(registros))
