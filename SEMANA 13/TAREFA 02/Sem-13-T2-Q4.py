def soma_cumulativa(lista):
    soma = 0
    lista_cumulativa = []
    for numero in lista:
        soma += numero
        lista_cumulativa.append(soma)
    return lista_cumulativa

def main():
    numeros = []
    
    while True:
        numero = float(input("Digite um número (0 para terminar): "))
        if numero == 0:
            break
        numeros.append(numero)
    
    resultado = soma_cumulativa(numeros)
    print("Lista original:", numeros)
    print("Soma cumulativa:", resultado)

if __name__ == "__main__":
    main()
