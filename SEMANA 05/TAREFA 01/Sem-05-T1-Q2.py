def calcular(lado):
    return area,perimetro

def main():
    lado=float(input('Digite o valor do lado de um quadrado: '))
    area=lado**2
    perimetro=lado*4
    print(f'A área do quadrado é: {area:10.4f}')
    print(f'O perímetro do quadrado é: {perimetro:10.4f}')

if __name__ == '__main__':
    main()
