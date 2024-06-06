def perguntas(p1,p2,p3,p4,p5):
    score = 0
    
    if p1 == 'S':
        score = score + 1
    
    if p2 == 'S':
        score = score + 1
        
    if p3 == 'S':
        score = score + 1
        
    if p4 == 'S':
        score = score + 1
        
    if p5 == 'S':
        score = score + 1
        
    if score == 2:
        return 'Suspeito'
    elif score == 3 or score == 4:
        return 'Cúmplice'
    elif score == 5:
        return 'Assassino'
    else:
        return 'Inocente'
    
def main():
    p1 = input().upper().strip()
    p2 = input().upper().strip()
    p3 = input().upper().strip()
    p4 = input().upper().strip()
    p5 = input().upper().strip()
    
    resultado=perguntas(p1,p2,p3,p4,p5)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
