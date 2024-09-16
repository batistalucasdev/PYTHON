def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.strip().split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    return resultado

def mes_para_texto(mes):
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    return meses.get(mes, "mês inválido")

def cidades_aniversario_e_populacao(mes, populacao, cidades):
    cidades_encontradas = [cidade for cidade in cidades if cidade[4] == mes and cidade[5] > populacao]
    if cidades_encontradas:
        print(f"CIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {mes_para_texto(mes).upper()}:")
        for cidade in cidades_encontradas:
            print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {mes_para_texto(mes)}.")
    else:
        print(f"Não há cidades com mais de {populacao} habitantes e aniversário em {mes_para_texto(mes).upper()}.")

def main():
    cidades = carrega_cidades()
    mes = int(input("Digite o mês do aniversário (1-12): "))
    populacao = int(input("Digite a população mínima: "))
    cidades_aniversario_e_populacao(mes, populacao, cidades)

if __name__ == "__main__":
    main()
