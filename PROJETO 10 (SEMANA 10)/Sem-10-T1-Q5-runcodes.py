def maior_numero(conjunto):
    maior = conjunto[0]
    for numero in conjunto:
        if numero > maior:
            maior = numero
    return maior

def main():
    conjunto = []
    for i in range(100):
        numero = int(input())
        conjunto.append(numero)
    
    conjunto_positivo = [num for num in conjunto if num > 0]
    if conjunto_positivo:
        maior = maior_numero(conjunto_positivo)
        print(f"{maior}")

if __name__ == "__main__":
    main()
