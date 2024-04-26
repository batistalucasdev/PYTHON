dist=int(input('Qual a distância até um planeta (em km)? '))
vel=int(input('Qual a velocidade da nave (em km/h)? '))
tempo=dist//vel
dias=tempo//24
horas=tempo%24
print('A viagem levará',dias,'dias e',horas,'horas')
