def verificacao(base,altura):

    if base == altura:
        return 'QUADRADO'
    elif base != altura:
        perimetro = str(2 * base + 2 * altura)
        area = str(base * altura)
        return f'{perimetro} - {area}'
    else:
        raise ValueError(f'Informação inválida')

def main():
    base=int(input())
    altura=int(input())
    
    resultado=verificacao(base,altura)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
