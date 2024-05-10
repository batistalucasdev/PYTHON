hora=int(input('Insira as horas: '))
minuto=int(input('Insira os minutos: '))
segundo=int(input('Insira os segundos: '))
hr=hora*3600
mnt=minuto*60
soma=hr+mnt+segundo
print(f'{soma} segundos se passaram no total desde a última meia-noite até a hora lida.')
