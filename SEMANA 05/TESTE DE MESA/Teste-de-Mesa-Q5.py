#5 Questão

#A função “minutos_para_horas” recebe o parâmetro “qtd_minutos”
def minutos_para_horas(qtd_minutos):
    #Retorna a quantidade de horas
    horas = qtd_minutos // 60
    #Retorna a quantidade de minutos
    minutos = qtd_minutos % 60
    #Retorna o valor equivalente de horas e minutos
    return f'{horas}h{minutos}min'

#A variável "minutos" recebe, convertido para inteiro, a leitura de minutos feita pelo teclado
minutos = int(input('Quantidade de minutos: '))
#A variável "horas" recebe a quantidade de minutos
horas = minutos_para_horas(minutos)
#Imprime na tela a quantidade de minutos e a quantidade de horas equivalente
print(f'{minutos} minutos são equivalentes a {horas}')
