def ler_numeros(qtd):
    numeros = []
    for i in range(qtd):
        numero = int(input())
        numeros.append(numero)
    return numeros

def encontrar_maior_e_posicao(lista):
    maior = lista[0]
    posicao = 0
    for i in range(1, len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao = i
    return maior, posicao

def main():
    qtd_numeros = 10
    numeros = ler_numeros(qtd_numeros)
    
    maior, posicao = encontrar_maior_e_posicao(numeros)
    
    print(numeros)
    print(maior)
    print(posicao)

if __name__ == "__main__":
    main()
