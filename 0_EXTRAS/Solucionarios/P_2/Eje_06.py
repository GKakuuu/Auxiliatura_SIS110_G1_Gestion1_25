# Montañas 

mont_simb = str(input("Ingrese la representacion de las montañas en simbolos(+ y -): "))

mont_num = []
cont = 0

for _ in range(len(mont_simb)):
    if mont_simb[_] == '+':
        cont += 1
        mont_num.append(cont)
        

    elif mont_simb[_] == '-':
        cont -= 1
        mont_num.append(cont)

print("Punto mas alto de la montaña: ", mont_num.index(max(mont_num)) + 1)


