#7 Questão

#A função “inverter” recebe o parâmetro “numero"
def inverter(numero):
    #Calcula o último dígito do número original
    u = numero % 10
    #Remove o último dígito do número original
    numero = numero // 10
    #Calcula o segundo dígito da direita para a esquerda
    d = numero % 10
    #Remove o segundo dígito da direita para a esquerda
    numero = numero // 10
    #Calcula o terceiro dígito da direita para a esquerda
    c = numero % 10
    #Remove o terceiro dígito da direita para a esquerda
    numero = numero // 10
    #O que resta do número será o primeiro dígito da esquerda
    m = numero % 10
    #Forma o número invertido a partir dos algarismos extraídos
    numero_invertido = (u * 1000) + (d * 100) + (c * 10) + m
    #Retorna o valor do número invertido
    return numero_invertido

#A variável "n" recebe, convertido para inteiro, a leitura do número feita pelo teclado
n = int(input("Digite um número entre 1000 e 9999: "))
#Imprime na tela o número lido e o inverso desse número
print(f'O inverso de {n} é {inverter(n)}')
