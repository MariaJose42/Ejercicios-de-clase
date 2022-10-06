#Realizar una función que devuelva True si es primo y False si no lo es.

def esPrimo(num):
    for i in range (2,num):
        if(num % i==0):
            return False
    
    return True
    
num=int(input("Dime un número: "))
print(esPrimo(num))