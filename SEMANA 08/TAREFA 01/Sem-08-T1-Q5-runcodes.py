def calcular_imc(massa,altura):
    imc=massa/altura**2

    if imc < 18.5:
        return 'Abaixo do peso'
    
    elif 18.5 <= imc < 25:
        return 'Peso normal'

    elif 25 <= imc < 30:
        return 'Sobrepeso'

    elif 30 <= imc < 35:
        return 'Obeso leve'
    
    elif 35 <= imc < 40:
        return 'Obeso moderado'
    
    elif imc >= 40:
        return 'Obeso mórbido'
    
def main ():
    massa=float(input())
    altura=float(input())
    imc=massa/altura**2
    resultado=calcular_imc(massa,altura)
    print(f'{imc:.2f}')
    print(f'{resultado}')

if __name__ == '__main__':
    main()
