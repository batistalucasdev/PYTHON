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
        valor = int(input())
        if valor == 0:
            break
        lista.append(valor)
    return lista

def main():
    lista = ler_lista()

    print(lista)
    print(comprimento(lista))
    print(inverter(lista))
    print(minimo(lista))
    print(maximo(lista))
    print(soma(lista))

if __name__ == "__main__":
    main()
