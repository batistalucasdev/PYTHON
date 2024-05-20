def ano_terrestre(idade):
    return idade//2

def main():
    idade=int(input())
    ano_espacial=ano_terrestre(idade)
    print(f'{ano_espacial}')

if __name__ == '__main__':
    main()
