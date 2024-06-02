def diferenca(num1,num2,num3):
    sub1 = abs(num1 - num2)
    sub2 = abs(num1 - num3)
    
    if sub1 > sub2:
        return sub2
    else:
        return sub1

def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    
    resultado=diferenca(num1,num2,num3)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
