cont = int(input("Cuantos numeros quieres ingresar: "))

cont_negro = 0
cont_blanco = 0
cont_color = 0

for i in range(cont):
    prenda = input("Introduce una prenda: ")
    
    if "negr" in prenda.lower():
        cont_negro = cont_negro + 1
    
    elif "blanc" in prenda.lower():
        cont_blanco = cont_blanco + 1
    
    else:
        cont_color = cont_color + 1
    
print(cont_negro)
print(cont_blanco)
print(cont_color)