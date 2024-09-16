def ler_lista(tamanho):
    lista = []
    for _ in range(tamanho):
        while True:
            try:
                num = int(input("Digite um número inteiro: "))
                lista.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    return lista

def eliminar_repetidos(lista):
    lista_sem_repetidos = []
    for item in lista:
        if item not in lista_sem_repetidos:
            lista_sem_repetidos.append(item)
    return lista_sem_repetidos

def main():
    tamanho = 20
    lista = ler_lista(tamanho)
    lista_sem_repetidos = eliminar_repetidos(lista)
    print("Lista original:", lista)
    print("Lista sem elementos repetidos:", lista_sem_repetidos)

if __name__ == "__main__":
    main()
