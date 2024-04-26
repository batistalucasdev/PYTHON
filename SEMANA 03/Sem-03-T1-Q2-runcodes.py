dist=int(input())
vel=int(input())
tempo=dist//vel
dias=tempo//24
horas=tempo%24
print(dias,'dias e',horas,'horas')
