def letra_musica(start, stop):
    for i in range(start, stop + 1, -11):
        if i == 1:
            print('1 bug no software, pegue onze deles e conserte...')
            print('Tecle "Ctrl+F5"')
        else:
            print(f'{i} bugs no software, pegue onze deles e conserte...')
            print('Tecle "Ctrl+F5"')
    print('Sem erros no software! Está estabilizado!')
    
def main():
    start = 99
    stop = 0
    letra_musica(start, stop)

if __name__ == "__main__":
    main()
