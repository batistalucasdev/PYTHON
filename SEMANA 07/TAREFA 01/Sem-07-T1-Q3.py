def digite_cor(cor):
    if cor=="V" or cor=="v":
        return "Siga"
    elif cor=="A" or cor=="a":
        return "Atenção"
    elif cor=="E" or cor=="e":
        return "Pare"

def main():
    cor=input('Digite a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho): ')
    sinal=digite_cor(cor)
    print(sinal)

if __name__ == '__main__':
    main()
