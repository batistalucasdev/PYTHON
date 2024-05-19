def horas(tempo):
    return tempo//3600

def minutos(tempo):
    return (tempo%3600)//60

def segundos(tempo):
    return tempo%60

def main():
    tempo=int(input())
    HH=horas(tempo)
    MM=minutos(tempo)
    SS=segundos(tempo)
    print(f'{HH}:{MM}:{SS}')

if __name__ == '__main__':
    main()
