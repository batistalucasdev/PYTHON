def par_impar(num):
    if num%2==0:
        return False
    else:
        return True

def main():
    num=int(input())
    numero=par_impar(num)
    print(numero)
    
if __name__ == '__main__':
    main()
