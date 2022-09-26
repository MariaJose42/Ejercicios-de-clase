#Introduciendo un número en el teclado, imprimir la tabla de multiplicar
#de dicho número.

def tabla_multiplicar (num):
    num = -1
    indice = 0
    
    while (indice<=10):
        res = indice*num
        print (num," x ", indice, " = ",resultado)
        indice +=1

num = int(input("Dime un número:"))
tabla_multiplicar(num)
