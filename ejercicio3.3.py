#Imprimir en pantalla el número mayor y el número menor de una serie
#de cinco números enteros que vamos introduciendo por teclado.

num1=-1
num2=-1
num3=-1
num4=-1
num5=-1
mayor = 0
menor = -1

#Preguntar números.
num1 = int(input ("Dime un número: "))
num2= int(input ("Dime un número: "))
num3 = int(input ("Dime un número: "))
num4 = int(input ("Dime un número: "))
num5 = int(input ("Dime un número: "))

if(num1>num2):
    mayor= num1
    menor= num2
else :
    mayor=num2
    menor=num1
    
if(mayor>num3):
    mayor= mayor
    menor= num3
else :
    mayor=num3
    menor=mayor
    
if(mayor>num4):
    mayor= mayor
    menor= num4
else :
    mayor=num4
    menor=mayor
    
if(mayor>num5):
    mayor= mayor
    menor= num5
else:
    menor=mayor
    mayor= num5
    
print ("El número mayor es",mayor,"y el menor es", menor,".")
    

    




