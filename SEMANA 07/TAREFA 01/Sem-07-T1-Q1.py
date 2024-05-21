def pessoa(gen):
    if gen==1:
        return "Ilmo Sr. "
    elif gen==2:
        return "Ilma Sra. "

def main():
    nome=input('Digite seu nome: ')
    gen=int(input('Digite "1" para sexo masculino e "2" para sexo feminino: '))
    sexo=pessoa(gen)
    print(sexo + nome)

if __name__ == '__main__':
    main()
