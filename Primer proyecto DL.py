def decbin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]

def hexdec(n):
    print(n) 
    n = int(n, base=16)
    return n

def Complemento2(n):
    #Invertimos los unos y los ceros (Complemento a1):
    for i in range(len(n)):
        if n[i]==0:
            n[i]=1
        elif n[i]==1:
            n[i]=0

    #Sumamos uno a la derecha (Complemento a2): 
    for i in range(7,-1,-1):  #Recorre la lista de derecha a izquierda, empieza en el indice 7, va hasta el indice 0 y decrementa en 1
        if n[i]==0:
            n[i]=1
            break
        elif n[i]==1:
            n[i]=0

def main():                
    bits=int(input("Seleccione numero de bit de los factores:"))
    print("Dijite un numero entre 0 y", (2**bits)-1)
    print("Digite antes del numero d:decimal, h:hexadecimal, b:binario")
    num1=input("Primer factor:")
    num2=input("Segundo factor:")
    notacion_num1 = num1[0]
    notacion_num2 = num2[0]
    
    num1 = switch_menu(notacion_num1, num1)
    num2 = switch_menu(notacion_num2, num2)

    print("binario factor 1",num1)
    print("binario factor 2",num2)
    
        

def switch_menu(notacion, num):
    print("notacion: ", notacion, " numero: ", num)
    if(notacion == 'b'):
        return int(num[1:])
    if(notacion == 'd'):
        num = decbin(int(num[1:]))
        return num
    if(notacion == 'h'):
        num = hexdec(num[1:])
        num = decbin(num)
        return num
    if(notacion.isdigit()):
        num = decbin(int(num))
        return num
    else:
        print('Revise la notacion de los factores')

main()


