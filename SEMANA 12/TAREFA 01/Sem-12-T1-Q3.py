def calcular_tempo_para_ultrapassar(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0
    while populacao_b <= populacao_a:
        populacao_a *= (1 + taxa_a)
        populacao_b *= (1 + taxa_b)
        anos += 1
    return anos

def main():
    taxa_crescimento_a = 0.02
    taxa_crescimento_b = 0.03

    populacao1 = float(input("Informe a primeira população: "))
    populacao2 = float(input("Informe a segunda população: "))

    if populacao1 > populacao2:
        populacao_a = populacao1
        populacao_b = populacao2
    else:
        populacao_a = populacao2
        populacao_b = populacao1

    anos = calcular_tempo_para_ultrapassar(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)
    
    print(f"Serão necessários {anos} anos para que a população do país B ultrapasse a do país A.")

if __name__ == "__main__":
    main()
