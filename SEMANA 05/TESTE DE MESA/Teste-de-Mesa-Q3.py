#3 Questão

#A função "area_quadrado" recebe o parâmetro "lado"
def area_quadrado(lado):
    #Retorna o valor do lado do quadrado multiplicado por ele mesmo
    return lado * lado

#A função "perimetro_quadrado" recebe o parâmetro "lado"
def perimetro_quadrado(lado):
    #Retorna o valor do lado do quadrado multiplicado por 4
    return lado * 4

#A variável "valor_lado" recebe, convertido para reais, a leitura do lado do quadrado feita pelo teclado
valor_lado = float(input('Lado do quadrado: '))
#Imprime na tela o valor da área do quadrado
print('Área do quadrado:',area_quadrado(valor_lado))
#Imprime na tela o valor do perímetro do quadrado
print('Perímetro do quadrado:',area_quadrado(valor_lado))
