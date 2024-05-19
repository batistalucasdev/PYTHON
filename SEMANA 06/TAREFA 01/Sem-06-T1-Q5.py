def pag_vista(valor):
    return valor-(valor*9/100)

def pag_5vezes(valor):
    return valor/5

def pag_10vezes(valor):
    return (valor+(valor*17/100))/10

def main():
    valor=int(input('Valor da compra: '))
    pagamento_vista=pag_vista(valor)
    pagamento_5vezes=pag_5vezes(valor)
    pagamento_10vezes=pag_10vezes(valor)
    print(f'O valor para pagamento à vista, com desconto de 9% é: {pagamento_vista:.2f}')
    print(f'O valor da prestação para pagamento em 5 vezes, sem desconto nem juros é: {pagamento_5vezes:.2f}')
    print(f'O valor da prestação para pagamento em 10 vezes, com 17% de juros é: {pagamento_10vezes:.2f}')

if __name__ == '__main__':
    main()
