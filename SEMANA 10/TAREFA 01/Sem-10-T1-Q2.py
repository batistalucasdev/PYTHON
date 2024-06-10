def contador(numeros):
    pares = 0
    impares = 0
    
    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

def main():
    print('Digite um conjunto de 100 números inteiros: ')
    numeros = []
    for i in range(100):
        entrada = input()
        numeros.append(int(entrada))

    pares, impares = contador(numeros)
    print(f'Esse conjunto possui {pares} números pares.')
    print(f'Esse conjunto possui {impares} números ímpares.')

if __name__ == "__main__":
    main()
