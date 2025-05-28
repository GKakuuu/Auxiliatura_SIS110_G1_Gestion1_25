# Una lavandería necesita separar prendas por colores a partir de sus nombres.
# Recibe N nombres de prendas y debe agruparlas por si contienen la palabra
# "blanco", "negro", o "color" (cualquier otro caso). 

cas = int(input("Ingrese la cantidad de prendas: "))

cont_blanco = 0
cont_negro = 0
cont_color = 0

for i in range (cas):
    prenda = str(input("Introduce una prenda: "))

    if "blanc" in prenda.lower():
        cont_blanco += 1
    
    elif "negr" in prenda.lower():
        cont_negro += 1
    
    else:
        cont_color += 1

print("Blancas: ", cont_blanco)
print("Negras: ", cont_negro)
print("Colores: ", cont_color)
