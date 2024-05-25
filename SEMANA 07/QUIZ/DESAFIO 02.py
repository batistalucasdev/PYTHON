print('''
Em que ano o filme Titanic foi lançado?
a - 1995
b - 1996
c - 1997
''')
resposta=input().lower()

if resposta == "a":
    print(" Resposta incorreta :// ")
elif resposta == "b":
    print(" Resposta incorreta! :( ")
elif resposta == "c":
    print(" Resposta certa! :) ")
else:
    print(" Você não escolheu a, b ou c :( ")
