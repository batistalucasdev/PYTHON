def horas(tempo):
    return tempo//3600

def minutos(tempo):
    return (tempo%3600)//60

def segundos(tempo):
    return tempo%60

def main():
    tempo=int(input('Digite o tempo de duração de um evento em uma fábrica expresso em segundos: '))
    HH=horas(tempo)
    MM=minutos(tempo)
    SS=segundos(tempo)
    print(f'Esse tempo corresponde a {HH}:{MM}:{SS}')

if __name__ == '__main__':
    main()
