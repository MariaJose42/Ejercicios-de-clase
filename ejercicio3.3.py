# Imprimir en pantalla el número mayor y el número menornde una serie de
# 5 números enteros que vamos introduciendo por teclado.

import math

#Inicializamos las variables.
num=-1
contador= 5 
min_=math.inf
max_=(-1)*math.inf


while(contador>0):
    num= int(input ("Dime un número: "))
    
    #comparar el minimo
    if(num<min_):
        min_= num
    #Comparamos el máximo
    if(num>max_):
        max_=num
        
    contador-= 1
   

print ("El máximo es:",max_)
print ("El mínimo es:",min_)