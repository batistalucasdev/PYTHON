#6 Questão

#A função “trocar” recebe os parâmetros “x1” e "x2"
def trocar(x1,x2):
    #Retorna os valores de x1 e x2
    return x1,x2

#A variável "n1" recebe, convertido para inteiro, a leitura do primeiro número feita pelo teclado
n1 = int(input('Primeiro número: '))
#A variável "n2" recebe, convertido para inteiro, a leitura do segundo número feita pelo teclado
n2 = int(input('Segundo número: '))
#As variáveis "n1" e "n2" recebem a função "trocar" e são atribuídos os valores de retorno a "n1" e "n2"
n1,n2 = trocar(n1,n2)
#Imprime na tela o primeiro e o segundo número
print(f'Primeiro {n1}; Segundo {n2}.')
