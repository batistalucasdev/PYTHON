def main():
    populacao_inicial = int(input("Digite a população de aves: "))
    populacao = populacao_inicial
    ano = 1600

    while populacao >= 0.1 * populacao_inicial:
        nascimentos = populacao * 1/100
        mortes = populacao * 6 / 100
        populacao = populacao - mortes + nascimentos

        print(f"{ano},{nascimentos:.0f},{mortes:.0f},{populacao:.0f}")
        
        ano += 1

if __name__ == "__main__":
    main()
