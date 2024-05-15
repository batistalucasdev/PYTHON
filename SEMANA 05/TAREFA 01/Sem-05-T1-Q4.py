def minutos (hora,sobra):
    return hora,sobra

def main():
    minutos=int(input('Digite a quantidade de minutos: '))
    hora=minutos//60
    sobra=minutos%60
    print(f'Isso corresponde a {hora}:{sobra}')

if __name__ == '__main__':
    main()
