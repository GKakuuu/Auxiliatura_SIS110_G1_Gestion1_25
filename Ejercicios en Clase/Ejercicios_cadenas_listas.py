# list_names = ["juan", "Gabriel", "jose"]

# string1 = "hola mundo"

# print(string1[::-1])

# # list_string = list(string1.upper())

# # print(list_string)

# # print(len(list_names))
# # print(len(string1))

list_numbers = []
for i in range(5):
    number = int(input("Introduce un numero: "))
    list_numbers.append(number) # agregar el numero a la lista

print(sum(list_numbers)) # suma de los elementos de la lista
print(max(list_numbers)) # maximo de la lista
print(min(list_numbers)) # minimo de la lista
print(list_numbers) # imprimir la lista
