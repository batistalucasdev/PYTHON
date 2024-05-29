def calcular_media(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5) / 5
    acima_da_media = [num for num in (num1, num2, num3, num4, num5) if num > media]
    return media, acima_da_media

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())

    media, acima_da_media = calcular_media(num1, num2, num3, num4, num5)

    print(f'{media:.2f}')
    for num in acima_da_media:
        print(num)

if __name__ == '__main__':
    main()
