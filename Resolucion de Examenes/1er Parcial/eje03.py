# 3. Leer un numero entero y determinar si es un numero par.
# Input      Output
# 2            si
# 3            no
# 4            si

int_num = int(input("Ingrese un numero entero: "))

if int_num % 2 == 0:
    print("si")
else:
    print("no")