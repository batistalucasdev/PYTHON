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
    altura=float(input("Digite sua altura (em metros): "))
    sexo=int(input("Digite seu sexo ('1' para homens e '2' para mulheres): "))

    resultado=calcular_peso_ideal(altura,sexo)
    print(f'O seu peso ideal é: {resultado:.2f} Kg')

if __name__ == '__main__':
    main()
