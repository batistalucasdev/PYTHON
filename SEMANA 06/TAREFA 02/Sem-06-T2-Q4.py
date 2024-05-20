def ano_terrestre(idade):
    return idade//2

def main():
    idade=int(input('Digite sua idade em ano(s) terrestre(s): '))
    ano_espacial=ano_terrestre(idade)
    print(f'Sua idade em anos terrestres é: {ano_espacial}')

if __name__ == '__main__':
    main()
