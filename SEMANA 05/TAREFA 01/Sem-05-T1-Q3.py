def percentual(valor,porcentagem):
    return valor*(porcentagem/100)

def main():
    v=float(input('Digite o preço: '))
    p=float(input('Digite o valor percentual: '))
    preco_aumento=v+(v*p/100)
    desconto=v-(v*p/100)
    print(f'O preço com aumento é: {preco_aumento:.2f}')
    print(f'O preço com desconto é: {desconto:.2f}')

if __name__ == '__main__':
    main()
