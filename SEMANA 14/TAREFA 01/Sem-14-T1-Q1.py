def comprimento(lista):
    count = 0
    for item in lista:
        count += 1
    return count

def inverter(lista):
    lista_invertida = []
    for i in range(comprimento(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

def minimo(lista):
    if comprimento(lista) == 0:
        return None
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

def maximo(lista):
    if comprimento(lista) == 0:
        return None
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total

def ler_lista():
    lista = []
    while True:
        valor = int(input("Digite um número (0 para encerrar): "))
        if valor == 0:
            break
        lista.append(valor)
    return lista

def main():
    lista = ler_lista()

    print("Lista:", lista)
    print("Comprimento da lista:", comprimento(lista))
    print("Lista invertida:", inverter(lista))
    print("Menor valor na lista:", minimo(lista))
    print("Maior valor na lista:", maximo(lista))
    print("Soma dos valores da lista:", soma(lista))

if __name__ == "__main__":
    main()
