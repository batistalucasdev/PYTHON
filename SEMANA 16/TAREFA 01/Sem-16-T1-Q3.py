def ler_matriz(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma_primeira_linha(matriz):
    return sum(matriz[0])

def soma_ultima_coluna(matriz):
    return sum(linha[-1] for linha in matriz)

def media_elementos(matriz):
    total_elementos = sum(len(linha) for linha in matriz)
    soma_total = sum(sum(linha) for linha in matriz)
    return soma_total / total_elementos

def menor_elemento(matriz):
    return min(min(linha) for linha in matriz)

def maior_elemento(matriz):
    return max(max(linha) for linha in matriz)

def main():
    n = int(input("Digite o número de linhas (n): "))
    m = int(input("Digite o número de colunas (m): "))
    
    matriz = ler_matriz(n, m)
    
    soma_primeira = soma_primeira_linha(matriz)
    soma_ultima = soma_ultima_coluna(matriz)
    media = media_elementos(matriz)
    menor = menor_elemento(matriz)
    maior = maior_elemento(matriz)
    
    resultado = (soma_primeira, soma_ultima, round(media, 4), menor, maior)
    print("Resultados:", resultado)

if __name__ == "__main__":
    main()
