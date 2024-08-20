from random import *

#essa variável deve ser alterada pelo usuário para terminar o jogo
jogando = True

score = 0

#imprime as instruções do jogo
print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

#repete enquanto a variável 'playing' for 'True'
while jogando == True:

    #escolhe um numero aleatoriamente entre 1 e 10
    novoNumero = randint(1,10)

    #soma o novo número à pontuação
    score = score + novoNumero

    #mostra os dados para o jogador
    print("\nSeu próximo número é", novoNumero)
    print("Sua pontuação agora é", score)

    #termina se o usuário digitar 'n'
    #ou se a pontuação for maior que 21
    print("\nGostaria de somar mais um número? (s/n)")
    resposta = input()
    if resposta.lower() == 'n' or score > 21:
        jogando = False
    
print("\nSua pontuação final é", score)

#se o jogador marcar 21
if score == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!")
