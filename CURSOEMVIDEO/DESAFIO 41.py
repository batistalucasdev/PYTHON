nascimento = int(input('Digite o ano de nascimento: '))
idade = 2024 - nascimento

if idade <= 9:
    print('MIRIM.')
elif idade > 9 and idade <= 14:
    print('INFANTIL.')
elif idade > 14 and idade <= 19:
    print('JÚNIOR.')
elif idade > 19 and idade <= 20:
    print('SÊNIOR.')
else:
    print('MASTER.')
