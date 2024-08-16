def ler_numeros():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        if numero > 0:
            numeros.append(numero)
    return numeros

def encontrar_maior(numeros):
    return max(numeros) if numeros else None

def encontrar_menor(numeros):
    return min(numeros) if numeros else None

def main():
    numeros = ler_numeros()
    if numeros:
        maior = encontrar_maior(numeros)
        menor = encontrar_menor(numeros)
        print(f"{maior}")
        print(f"{menor}")
    else:
        print()

if __name__ == "__main__":
    main()
