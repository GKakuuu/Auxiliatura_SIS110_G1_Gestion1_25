# Cochalo estaba muy orgullosa del texto de un millón de palabras que escribió para su tarea.
# Lo estaba, hasta que se dio cuenta de que debía entregarse en una sola hoja de papel con
# dimensiones limitadas. Obviamente, podría haber acortado el texto, pero Cochalo decidió
# tomar otra opción. Decidió copiar el texto a una nueva hoja de papel, escribiendo un poco
# más pequeño ... Para facilitarlo, decidió cambiar primero los saltos de línea de su texto
# para que la suma de la altura y el ancho de la hoja de papel se minimizara. Dado el texto
# de Cochalo con n palabras y suponiendo que cada carácter ocupa una unidad de altura y una
# unidad de ancho, ¿cuál es la altura y el ancho mínimos que se pueden lograr insertando
# saltos de línea? Ten en cuenta que dos palabras que están en la misma línea deben estar
# separadas por un solo espacio.

# Entrada
# La entrada consta de:
# · Una línea con un entero n (1 <= n <= 10^6), el número de palabras
# · Una línea con n palabras separadas por espacios w (1 ≤ |w| ≤ 106), compuesta
# únicamente por letras latinas minúsculas.

# Se garantiza que la longitud total del texto, es decir, la suma de las longitudes de las
# n palabras, no sea mayor que 10^6

# Salida
# Genere un único entero: la suma de la altura y el ancho de la hoja de papel más pequeña
# donde quepa el texto.

# input                                           output
# 4                                               11
# i am lord voldemort

# 10                                              14
# i solomnly swear that i am up to no good

# Explanation
# These are visualizations of the optimal result
# first testcse: 2 + 9
# i_am_lord
# voldemort

n = int(input("Enter number of words: "))
words = input("Enter the words: ").split()

# Obtenemos la longitud de la palabra más larga haciendo un recorrido por la lista de palabras
max_word_len = max(len(word) for word in words) 

# obtenemos la suma de las longitudes de las palabras más los espacios entre ellas
total_chars = sum(len(word) for word in words) + (n - 1) 

min_sum = float('inf') # Inicializamos min_sum con infinito

for width in range(max_word_len, total_chars + 1):
    lines = 1
    curr_len = 0
    # Recorremos las palabras para calcular el número de líneas necesarias
    for word in words:
        if curr_len == 0:
            curr_len = len(word)

        elif curr_len + 1 + len(word) <= width:
            curr_len += 1 + len(word)

        else:
            lines += 1
            curr_len = len(word)

    min_sum = min(min_sum, lines + width)
print(min_sum)