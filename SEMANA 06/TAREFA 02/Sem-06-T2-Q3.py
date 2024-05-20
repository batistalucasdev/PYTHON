def preco_maca(maca):
    return maca*3

def preco_banana(banana):
    return banana*2

def main():
    maca=float(input('Digite o preço da maçã: '))
    banana=float(input('Digite o preço da banana: '))
    total=preco_maca(maca)+preco_banana(banana)
    print(f'Total da sua compra: {total:.2f}')

if __name__ == '__main__':
    main()
