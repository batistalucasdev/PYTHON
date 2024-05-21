def digite_cor(cor):
    if cor=="V" or cor=="v":
        return "Siga"
    elif cor=="A" or cor=="a":
        return "Atenção"
    elif cor=="E" or cor=="e":
        return "Pare"

def main():
    cor=input()
    sinal=digite_cor(cor)
    print(sinal)

if __name__ == '__main__':
    main()
