def letra_musica(start, stop):
    for i in range(start, stop + 1, 7):
        if i == 1:
            print('1 bug no software, pegue sete deles e conserte...')
            print('Tecle "Ctrl+F5"')
        else:
            print(f'{i} bugs no software, pegue sete deles e conserte...')
            print('Tecle "Ctrl+F5"')
    print('Vamos fazer mais um café!')
    
def main():
    start = 99
    stop = 250
    letra_musica(start, stop)

if __name__ == "__main__":
    main()
