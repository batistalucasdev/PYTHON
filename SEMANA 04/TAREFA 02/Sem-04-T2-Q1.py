num1=float(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))
num1str=str(num1)
num2str=str(num2)
soma=num1+num2
concatenacao=num1str+num2str
multiplicacao=num1*num2
multiplicacao_string=num1str*num2
divisao=num1/num2
divisao_inteira=num1//num2
exponenciacao=num1**num2
resto=num1%num2
print(f'A soma desses números é: {soma}')
print(f'A concatenação desses números é: {concatenacao}')
print(f'A multiplicação desses números é: {multiplicacao}')
print(f'A multiplicação como strings desses números é: {multiplicacao_string}')
print(f'A divisão desses números é: {divisao}')
print(f'A divisão inteira desses números é: {divisao_inteira}')
print(f'A exponenciação desses números é: {exponenciacao}')
print(f'O módulo (resto) desses números é: {resto}')
