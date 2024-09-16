def ler_lista(tamanho):
    lista = []
    print(f"Digite {tamanho} números reais:")
    for i in range(tamanho):
        while True:
            try:
                numero = float(input(f"Elemento {i + 1}: "))
                lista.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número real.")
    return lista

def produto_escalares(lista_x, lista_y):
    produto = 0
    for x, y in zip(lista_x, lista_y):
        produto += x * y
        expressoes.append(f"({int(x)} x {int(y)})")
    return produto, expressoes

def main():
    tamanho = 5
    
    print("Conjunto X:")
    lista_x = ler_lista(tamanho)
    
    print("Conjunto Y:")
    lista_y = ler_lista(tamanho)
    
    produto, expressoes = produto_escalares(lista_x, lista_y)
    
    print("\nConjunto X:", [int(x) for x in lista_x])
    print("Conjunto Y:", [int(y) for y in lista_y])
    print(f"{' + '.join(expressoes)} = {int(produto)}")

if __name__ == "__main__":
    main()
