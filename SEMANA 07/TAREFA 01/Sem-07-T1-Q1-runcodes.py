def pessoa(gen):
    if gen==1:
        return "Ilmo Sr. "
    elif gen==2:
        return "Ilma Sra. "

def main():
    nome=input()
    gen=int(input())
    sexo=pessoa(gen)
    print(sexo + nome)

if __name__ == '__main__':
    main()
