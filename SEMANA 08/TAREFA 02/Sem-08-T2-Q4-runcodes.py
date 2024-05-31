def calcular_peso_ideal(altura,sexo):
    homens = (72.7 * altura) - 58
    mulheres = (62.1 * altura) - 44.7

    if sexo == 1:
        return homens
    elif sexo == 2:
        return mulheres
    else:
        raise ValueError(f'Sexo informado inválido: {sexo}')

def main():
    altura=float(input())
    sexo=int(input())

    resultado=calcular_peso_ideal(altura,sexo)
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
