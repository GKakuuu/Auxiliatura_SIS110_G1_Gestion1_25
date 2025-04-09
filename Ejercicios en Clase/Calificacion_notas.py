nota = int(input("Introducir una nota: "))

if (0 <= nota < 51):
    print("malo")
elif (51 <= nota <= 60):
    print("regular")
elif (61 <= nota <= 75):
    print("bueno")
elif (76 <= nota <= 90):
    print("muy bueno")
else:
    print("excelente")
    