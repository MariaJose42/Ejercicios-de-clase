#Decir si un número es primo.
'''
esPrimo(13)
     True
     
esPrimo(8)
     False'''

contador = 0
num= -1
resultado=0

num= int(input("Dime un número: "))

while (contador < num):
    contador+=1
    if (num%contador==0):
        resultado +=1
    else:
        resultado=resultado
if(resultado==2):
    print("Es primo.")
else:
    print("No es primo.")
    

    
    
