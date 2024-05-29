def calcular_media(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5) / 5
    acima_da_media = [num for num in (num1, num2, num3, num4, num5) if num > media]
    return media, acima_da_media

def main():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    num3=int(input("Digite o terceiro número: "))
    num4=int(input("Digite o quarto número: "))
    num5=int(input("Digite o quinto número: "))

    media, acima_da_media = calcular_media(num1, num2, num3, num4, num5)

    print(f'A média é: {media:.2f}')
    print(f'Os números maiores que a média são: ')
    for num in acima_da_media:
        print(num)

if __name__ == '__main__':
    main()
