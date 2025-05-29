word = str(input("Introduce una palabra: "))

print("la palabra en mayusculas es: ", word.upper())
print("la palabra en minusculas es: ", word.lower())

for i in range(len(word)):
    print(word[i], end=" ")

print("\nla palabra al reves es: ", word[::-1])

if "hola" in word:
    print("la palabra contiene la cadena 'hola'")

