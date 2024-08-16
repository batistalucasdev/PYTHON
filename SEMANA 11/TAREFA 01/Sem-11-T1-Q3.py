def ler_numeros():
    numeros = []
    while True:
        numero = int(input("Digite um número inteiro positivo (0 para terminar): "))
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
        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    else:
        print("Nenhum número válido foi inserido.")

if __name__ == "__main__":
    main()
