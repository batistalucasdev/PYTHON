def calcular_media(numeros):
    if numeros:
        return sum(numeros) / len(numeros)
    return None

def main():
    numeros = []
    
    while True:
        numero = int(input())
        if numero == 0:
            break
        if numero > 0:
            numeros.append(numero)
        else:
            print()
    
    media = calcular_media(numeros)
    if media is not None:
        print(f"{media:.2f}")
    else:
        print()

if __name__ == "__main__":
    main()
