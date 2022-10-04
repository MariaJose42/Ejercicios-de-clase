#Devolver la suma de los diez primeros números naturales.

'''contador = 0
num= 0 

while (contador<=10):
    num+=contador
    contador+=1
    
print("El total es: ",num)'''

#Devolver la suma de los n primeros números naturales.

contador = 0
num= 0
num1= 0

num1= int(input("Dime un número: "))

while(contador<=num1):
    num+=contador
    contador+=1
    
print("El total es: ",num)

def suma_total(n):
    contador=0
    acumulador=0
    while(contador<n):
        contador +=1
        acumulador+=contador
    print("El total es: ",acumulador)    




