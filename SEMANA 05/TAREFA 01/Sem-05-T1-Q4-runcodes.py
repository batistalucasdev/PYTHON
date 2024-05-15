def minutos (hora,sobra):
    return hora,sobra
minutos=int(input())
hora=minutos//60
sobra=minutos%60
print(f'{hora}:{sobra}')

