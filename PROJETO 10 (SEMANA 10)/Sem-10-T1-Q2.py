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
    numeros = []
    for i in range(100):
        entrada = input()
        numeros.append(int(entrada))

    pares, impares = contador(numeros)
    print(pares)
    print(impares)

if __name__ == "__main__":
    main()
