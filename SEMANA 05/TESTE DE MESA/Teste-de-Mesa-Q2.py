#2 Questão

#A função "eh_par" recebe o parâmetro "numero"
def eh_par(numero):
    #Retorna o valor da divisão de um número por 2, com resto igual a 0
    return numero % 2 == 0

#Imprime o valor booleano para o número 2
print('2 é par?',eh_par(2))
#Imprime o valor booleano para o número 3
print('3 é par?',eh_par(3))
#Imprime o valor booleano para o número 5
print('5 é ímpar?',eh_par(5))
