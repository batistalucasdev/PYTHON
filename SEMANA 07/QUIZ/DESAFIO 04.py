print('''
1) Em que ano o filme Titanic foi lançado?
a - 1995
b - 1996
c - 1997
''')

resposta=input().lower()
score=0

if resposta == "a":
    print(" Resposta incorreta :( ")
elif resposta == "b":
    print(" Resposta incorreta! :( ")
elif resposta == "c":
    print(" Resposta certa! :) ")
else:
    print(" Você não escolheu a, b ou c :// ")

if resposta == 'c':
    score = score + 1

print('''
2) Qual é o nome do personagem principal masculino de Titanic?

a - Jack Dawson
b - Caledon "Cal" Hockley
c - Fabrizio De Rossi
''')

resposta=input().lower()

if resposta == "a":
    print(" Resposta certa :) ")
elif resposta == "b":
    print(" Resposta incorreta! :( ")
elif resposta == "c":
    print(" Resposta incorreta! :( ")
else:
    print(" Você não escolheu a, b ou c :// ")

if resposta == 'a':
    score = score + 1

print('''
3) Qual é o nome do personagem principal feminino de Titanic?

a - Ruth DeWitt Bukater
b - Rose DeWitt Bukater
c - Margaret "Molly" Brown
''')

resposta=input().lower()

if resposta == "a":
    print(" Resposta incorreta :( ")
elif resposta == "b":
    print(" Resposta certa! :) ")
elif resposta == "c":
    print(" Resposta incorreta! :( ")
else:
    print(" Você não escolheu a, b ou c :// ")

if resposta == 'b':
    score = score + 1
    
print(f" Você fez {score} ponto(s)! ")
if score == 3:
    print(" Muito bem! Você acertou todas as respostas :) ")
else:
    print(" Não desista! Tente novamente. ")
