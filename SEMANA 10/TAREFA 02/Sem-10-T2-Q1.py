def letra_musica(start, stop):
    for i in range(start, stop + 1):
        if i == 1:
            print("1 bug no software, pegue ele e conserte...")
        else:
            print(f"{i} bugs no software, pegue um deles e conserte...")

def main():
    start = 99
    stop = 250
    letra_musica(start, stop)

if __name__ == "__main__":
    main()
