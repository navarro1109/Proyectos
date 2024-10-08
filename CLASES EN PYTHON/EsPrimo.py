def es_primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            print(n, " no es primo")
            return False
    return True

n = int(input("Ingrese un número:\n"))
if es_primo(n):
    print(n, " es primo")