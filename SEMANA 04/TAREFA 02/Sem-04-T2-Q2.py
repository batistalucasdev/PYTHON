ano=int(input('Digite sua idade em anos: '))
mes=int(input('Digite sua idade em meses: '))
dias=int(input('Digite sua idade em dias: '))
ano_dias=ano*365
mes_dias=mes*30
idade=ano_dias+mes_dias+dias
print(f'Sua idade expressa em dias é: {idade}')
