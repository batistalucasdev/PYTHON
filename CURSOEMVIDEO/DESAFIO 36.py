valor_casa=float(input('Qual o valor da casa? '))
salario=float(input('Qual seu salário? '))
anos=int(input('Em quantos anos você vai pagar? '))

prestacao=valor_casa/(anos*12)

minimo=salario*30/100

print(f'Para pagar uma casa de {valor_casa:.2f} em {anos} anos', end='')
print(f' a prestação será de R${prestacao:.2f}')

if prestacao <= minimo:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo recusado!')
