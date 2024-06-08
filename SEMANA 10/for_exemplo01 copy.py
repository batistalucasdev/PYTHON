print('Comando 1')
print('Comando 2')
print('Comando 3')
print('Comando 4')
print('Comando 5')

if True:
    print('Comando 6')
    print('Comando 7')

print('Comando 8')

if True: print('Comando 9')

if False:
    print('Comando 10 (não executa)')
    print('Comando 11 (não executa)')

if False: print('Comando 12 (não executa)')

print('Comando 10')
print('Comando 11')
print('Comando 12')

for i in range(3):
    print(f'Comando 13 (i={i})')

for j in range(3): print(f'Comando 14 (j={j})')

def e_par(n): return n % 2 == 0

for k in range(1,11): #k vai de 1 a 10
    if not e_par(k): print(f'Comando 15 (k={k})')

    if e_par(k):
        print(f'Comando 16 (k={k})')

for i in range(3):
    for j in range(3):
        print(f'Comando 17 (i={i}, j={j})')
        print(f'Comando 18 (i={i}, j={j})')
    print(f'Comando 19 (i={i}, j={j})')
    print(f'Comando 20 (i={i}, j={j})')
print('Último comando')



        
