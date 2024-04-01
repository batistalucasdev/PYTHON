nascimento = int(input('Digite o ano de nascimento: '))
idade = 2024- nascimento

if idade < 18:
    tempo_falta = 18 - idade
    print('Ainda vai se alistar ao serviço militar.')
    print('Faltam',tempo_falta,'anos.')
elif idade == 18:
    print('É a hora de se alistar.')
else:
    tempo_passou = idade - 18
    print('Já passou do tempo de alistamento.')
    print('Passou',tempo_passou,'anos.')
