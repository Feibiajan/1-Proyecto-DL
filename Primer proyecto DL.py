def decbin(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]

def hexdec(n):
	numero = int(input(n))
	convertido = hex(numero)[2:]
	print(convertido)

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
                
bits=int(input("Seleccione numero de bit de los factores:"))
print("Dijite un numero entre 0 y", (2**bits)-1)
print("Digite antes del numero d:decimal, h:hexadecimal, b:binario")
num1=input("Primer factor:")
num2=input("Segundo factor:")
fac1=list(num1)
fac2=list(num2)
x=fac1[1:]
y=fac2[1:]
print(x)
print(y)
z = [int(i) for i in x]
o = [int(i) for i in y]
print(z)
print(o)
pen=z[0:]
print(pen)
#for i in fac1:
#    if 
#   if num1==0 or num==2:
#     print
#print(,-,)

