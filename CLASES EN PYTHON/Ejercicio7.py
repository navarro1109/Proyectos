
entero = True

while entero:
    try:
        num = input("Ingresa un número: \n")
        num = int(num)
        break
    except:
        print("El número debe ser entero.")

i = 1

while i <= 10:
    tabla = num * i
    print(num, "*", i, "=", tabla)
    i += 1
