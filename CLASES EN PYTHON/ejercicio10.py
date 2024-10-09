import random
import string

def generar_contraseña(longitud):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation


    if longitud < 8:
        print("La longitud mínima de la contraseña debe ser 8 caracteres.")
        return None

    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    todos_caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña += [random.choice(todos_caracteres) for _ in range(longitud - 4)]

    random.shuffle(contraseña)

    return ''.join(contraseña)

while True:
    try:
        longitud = int(input("Ingresa la longitud de la contraseña (mínimo 8 caracteres): "))

        contra_generada = generar_contraseña(longitud)
        if contra_generada:
            print("Contraseña generada: ", contra_generada)
            break
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
