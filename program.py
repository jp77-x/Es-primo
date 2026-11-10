def es_primo(numero):
    if numero <= 1:
        return False

    limite = int(numero ** 0.5) + 1

    for i in range(2, limite):
        if numero%i == 0:
            return False

    return True

num = int(input("Introduce un número para verificar si es primo: "))

if es_primo(num):
    print(f"El número {num} SÍ es primo.")
else:
    print(f"El número {num} NO es primo.")

def imprimir_primos(inicio, fin):
    for i in range(inicio, fin+1):
        if es_primo(i):
            print(i)

imprimir_primos(1, 100)