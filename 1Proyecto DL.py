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

def negacion(n,m):
    if n == "s":
        m=-int(m,2)
        return m
    else:
        m=int(m,2)
        return m

def main():
    bits=int(input("Seleccione numero de bit de los factores:"))
    nbi=(2**bits)-1
    print("Dijite un numero entre 0 y", nbi)
    print("Digite antes del numero d:decimal, h:hexadecimal, b:binario")
    neg1=input("Si el primer factor es negativo presione s: ")
    neg2=input("Si el segundo factor es negativo presione s: ")
    num1=input("Primer factor:")
    num2=input("Segundo factor:")
    nota_num1 = num1[0]
    nota_num2 = num2[0]
    bin1 = switch_menu(nota_num1, num1)
    bin2 = switch_menu(nota_num2, num2)
    op1=negacion(neg1,bin1)
    op2=negacion(neg2,bin2)
    print("notacion: ", nota_num1, " numero: ", op1)
    print("notacion: ", nota_num2, " numero: ", op2)
    print("binario factor 1",bin1)
    print("binario factor 2",bin2)
    mulbin(op1,op2)
    
def mulbin(x,y):
    result = 0
    print(decbin(x))
    print(decbin(y))
    print("-----------------")
    while y != 0:
        if (y) & 1:
            print(decbin(x))
            result += x
        else:
            print(0);
        print("--------------")
        print(decbin(result))
        x <<= 1
        y >>= 1
    print("Resultado en decimal", result)
    print("Resultado binario",decbin(result))

        

def switch_menu(notacion, num):
    if(notacion == 'b'):
        return num[1:]
    if(notacion == 'd'):
        num = decbin(int(num[1:]))
        return num
    if(notacion == 'h'):
        num = hexdec(num[1:])
        num = decbin(num)
        return num
    if(notacion.isdigit()):
        num = decbin(int(num))
        notacion = "."
        return num
    else:
        print('Revise la notacion de los factores')
main()


