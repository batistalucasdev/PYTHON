def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def maior_temperatura(temp1, temp2):
    valor1, escala1 = temp1
    valor2, escala2 = temp2
    
    if escala1 == escala2:
        if valor1 > valor2:
            return temp1
        else:
            return temp2
    else:
        if escala1 == 'C':
            valor1_convertido = celsius_to_fahrenheit(valor1)
            if valor1_convertido > valor2:
                return temp1
            else:
                return temp2
        else:
            valor2_convertido = celsius_to_fahrenheit(valor2)
            if valor1 > valor2_convertido:
                return temp1
            else:
                return temp2

def main():
    temp1 = (float(input("Temperatura 1: ")), input("Escala (C/F): ").upper()[0])
    temp2 = (float(input("Temperatura 2: ")), input("Escala (C/F): ").upper()[0])

    maior = maior_temperatura(temp1, temp2)
    print(maior)

if __name__ == "__main__":
    main()
