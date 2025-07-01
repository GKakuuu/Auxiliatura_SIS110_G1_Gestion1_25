# El Ing. Isaac Clarke se encuentra atrapado en el USG Ishimura (United Spacefaring Guild Ishimura),
# se enfrenta a diferentes tipos de enemigos, cada uno con su propio nivel de peligrosidad. Necesita
# implementar un software en su DRI (Dispositivo Integrador de Recursos) que simule un sistema de
# niveles para los enemigos a los que se enfrenta, así para tener una idea si es seguro o no entrar en
# combate; considera las siguientes condiciones:
# • Cada enemigo tiene un nivel de peligrosidad representado por un número entero entre 1 y 5.
# • Isaac puede encontrarse con hasta 10 enemigos en una zona.
# • Isaac puede usar un arma especial que tiene diferentes efectividades contra enemigos de
# diferentes niveles. El nivel de efectividad se representa como un número entre 1 y 10, donde
# 10 es completamente efectivo y 1 es menos efectivo.
# • Cada vez que Isaac se encuentre un enemigo, el programa con una IA deberá preguntarle el
# nivel de peligrosidad de cada enemigo (1-5) y el nivel de efectividad de su arma (1-10, siendo
# el mismo para cada enemigo) para así poder calcular y mostrar el daño posible de infligir al
# enemigo/s utilizando la fórmula: daño = nivel_efectividad * nivel_peligrosidad.
# • Si el daño es mayor o igual a 35, su DRI deberá mostrar un mensaje de "Es seguro entrar en
# combate", caso contrario deberá mostrar "ADVERTENCIA: Enemigos demasiado peligrosos".
# • Después de enfrentar a cada enemigo, el programa deberá preguntar si se desea continuar
# enfrentándose a más enemigos. Si Isaac decide no continuar, se mostrará un resumen de la
# misión.

def main():
    enemigos_enfrentados = 0
    resumen = []
    print("=== Sistema de Evaluación de Combate DRI ===")
    while enemigos_enfrentados < 10:
        try:
            nivel_peligrosidad = int(input(f"Ingrese el nivel de peligrosidad del enemigo #{enemigos_enfrentados+1} (1-5): "))
            if nivel_peligrosidad < 1 or nivel_peligrosidad > 5:
                print("Nivel de peligrosidad inválido. Debe estar entre 1 y 5.")
                continue
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            continue

        try:
            nivel_efectividad = int(input("Ingrese el nivel de efectividad de su arma (1-10): "))
            if nivel_efectividad < 1 or nivel_efectividad > 10:
                print("Nivel de efectividad inválido. Debe estar entre 1 y 10.")
                continue
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            continue

        dano = nivel_efectividad * nivel_peligrosidad
        resumen.append((enemigos_enfrentados+1, nivel_peligrosidad, nivel_efectividad, dano))
        print(f"Daño posible a infligir: {dano}")

        if dano >= 35:
            print("Es seguro entrar en combate")
        else:
            print("ADVERTENCIA: Enemigos demasiado peligrosos")

        enemigos_enfrentados += 1
        continuar = input("¿Desea continuar enfrentándose a más enemigos? (s/n): ").strip().lower()
        if continuar != 's':
            break

    print("\n=== Resumen de la misión ===")
    for num, nivel_p, nivel_e, dano in resumen:
        print(f"Enemigo #{num}: Peligrosidad={nivel_p}, Efectividad={nivel_e}, Daño={dano}")
    print(f"Total de enemigos enfrentados: {enemigos_enfrentados}")

if __name__ == "__main__":
    main()
