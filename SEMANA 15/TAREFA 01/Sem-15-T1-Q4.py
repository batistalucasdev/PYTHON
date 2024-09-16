def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.strip().split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    return resultado

def cidades_maior_populacao(populacao, cidades):
    cidades_encontradas = [cidade for cidade in cidades if cidade[5] > populacao]
    if cidades_encontradas:
        print(f"CIDADES COM MAIS DE {populacao} HABITANTES:")
        for cidade in cidades_encontradas:
            print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")
    else:
        print(f"Não há cidades com população maior que {populacao} habitantes.")

def main():
    cidades = carrega_cidades()
    populacao = int(input("Digite a população mínima: "))
    cidades_maior_populacao(populacao, cidades)

if __name__ == "__main__":
    main()
