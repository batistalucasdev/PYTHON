def ler_numeros():
    numeros = []
    for _ in range(20):
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    return numeros

def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def imprimir_listas(numeros, pares, impares):
    print("Lista completa:", numeros)
    print("Números pares:", pares)
    print("Números ímpares:", impares)

def main():
    numeros = ler_numeros()
    pares, impares = separar_pares_impares(numeros)
    imprimir_listas(numeros, pares, impares)

if __name__ == "__main__":
    main()
