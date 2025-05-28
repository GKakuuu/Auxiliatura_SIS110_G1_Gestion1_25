# Un viejo manuscrito mágico contiene una cadena de caracteres. El sabio de la aldea
# ha revelado que hay una letra secreta que debe aparecer exactamente dos veces en
# el mensaje para liberar al dragón guardián. 
# Tu tarea es detectar si alguna letra del abecedario minúsculo aparece exactamente
# dos veces. Si hay varias, muestra la primera en orden alfabético. Si no hay ninguna,
# imprime "Sin liberación". 

# Entrada: 
# • Una cadena con solo letras minúsculas (sin espacios). 
# Salida: 
# • Letra que aparece exactamente dos veces, la menor en orden alfabético. 
# • Si no hay ninguna, imprime "Sin liberación".

from collections import Counter

mensaje = input()
contador = Counter(mensaje)
print(contador)

letras_dos = [letra for letra in sorted(contador) if contador[letra] == 2]

if letras_dos:
    print(letras_dos[0])
else:
    print("Sin liberación")