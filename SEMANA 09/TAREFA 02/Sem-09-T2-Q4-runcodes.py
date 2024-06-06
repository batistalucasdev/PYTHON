def frutas(morango,maca):
    
    if morango <= 5:
        preco_morango = morango * 2.5
    else:
        preco_morango = morango * 2.2

    if maca <= 5:
        preco_maca = maca * 1.8
    else:
        preco_maca = maca * 1.5

    preco = preco_morango + preco_maca
    
    if morango + maca > 8 or preco > 25:
        preco = preco - preco * 10/100

    return preco
   
def main():
    morango=float(input())
    maca=float(input())
    
    resultado=frutas(morango,maca)
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()

