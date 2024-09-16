def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

lista = []
print("Digite os números para a lista. Digite 0 para encerrar.")
while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    lista.append(numero)

valor = int(input("Digite o valor a ser pesquisado na lista: "))

resultado = contar_ocorrencias(lista, valor)

print("\nLista:", lista)
print("Valor pesquisado:", valor)
print("Número de ocorrências do valor na lista:", resultado)

if __name__ == "__main__":
    main()
