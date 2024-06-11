def valor_compra(valor):
    parcela = 1000  

    for i in range(1, 25):
        parcela = valor / i
        print(f'{i}x de R$ {parcela:.2f}')
    
def main():
    valor = int(input())
    valor_compra(valor)

if __name__ == "__main__":
    main()
