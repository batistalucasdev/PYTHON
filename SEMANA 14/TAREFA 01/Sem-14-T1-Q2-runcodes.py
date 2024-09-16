def contar_ocorrencias(lista, valor):
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    return contador

lista = []
while True:
    numero = int(input())
    if numero == 0:
        break
    lista.append(numero)

valor = int(input())

resultado = contar_ocorrencias(lista, valor)

print(lista)
print(valor)
print(resultado)

if __name__ == "__main__":
    main()
