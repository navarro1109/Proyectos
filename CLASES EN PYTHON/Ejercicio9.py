import random

def adivinar_numero():
    numero = random.randint(1, 100)
    intentos = 0

    print("¡Adivina el número entre 1 y 100!")

    while True:
        try:
            adivinanza = int(input("Ingresa tu intento: "))
            intentos += 1

            if adivinanza > numero:
                print("El numero es menor...")
            elif adivinanza < numero:
                print("Intenta con un numero mayor...")
            else:
                print("¡Felicidades! Adivinaste el número en", intentos, " intentos.")
                break 
        except ValueError:
            print("El numero debe ser entero.")

adivinar_numero()
