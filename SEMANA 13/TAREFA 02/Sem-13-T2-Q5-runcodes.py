def esta_ordenado(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def main():
    n = int(input())
    lista = []

    for _ in range(n):
        elemento = float(input())
        lista.append(elemento)

    if esta_ordenado(lista):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")

if __name__ == "__main__":
    main()
