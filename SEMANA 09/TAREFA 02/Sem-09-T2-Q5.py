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
    p1=input("Telefonou para a vítima ? ").upper().strip()
    p2=input("Esteve no local do crime ? ").upper().strip()
    p3=input("Mora perto da vítima ? ").upper().strip()
    p4=input("Devia para a vítima ? ").upper().strip()
    p5=input("Já trabalhou com a vítima ? ").upper().strip()
    
    resultado=perguntas(p1,p2,p3,p4,p5)
    print(f'A classificação sobre a participação da pessoa no crime é: {resultado}')

if __name__ == '__main__':
    main()
