print("Em que ano você nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano você quer saber sua idade?")
ano = input()
ano = int(ano)
idade = ano - nascimento
print("Em", ano, "você terá", idade, "anos!")
