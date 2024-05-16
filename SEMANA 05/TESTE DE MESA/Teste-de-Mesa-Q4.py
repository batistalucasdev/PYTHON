#4 Questão

#A função "percentual" recebe os parâmetros "valor" e “porcentagem”
def percentual(valor,porcentagem):
    #Retorna o valor multiplicado pela porcentagem divido por 100
    return valor * (porcentagem / 100)

#A variável "pr" recebe, convertido para real, a leitura do preço feita pelo teclado
pr = float(input("Preço: "))
#A variável "vr_p" recebe, convertido para real, a leitura do percentual feita pelo teclado
vr_p = float(input("Percentual: "))
#A variável "pr_acres" recebe o resulado da fórmula do preço com acréscimo
pr_acres = pr + percentual(pr,vr_p)
#A variável "pr_desc" recebe o resulado da fórmula do preço com desconto
pr_desc = pr - percentual(pr,vr_p)
#Imprime na tela o percentual de acréscimo e o preço com acréscimo
print(f'R${pr} com acréscimo de {vr_p}% fica por R${pr_acres}')
#Imprime na tela o percentual de desconto e o preço com desconto
print(f'R${pr} com desconto de {vr_p}% fica por R${pr_desc}')
