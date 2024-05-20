def temperatura(celsius):
    return (celsius*(9/5))+32

def main():
    celsius=float(input('Digite a temperatura em graus Celsius (˚C): '))
    fahrenheit=temperatura(celsius)
    print(f'Essa temperatura em graus Fahrenheit (˚F) é: {fahrenheit:.2f}')

if __name__ == '__main__':
    main()
