#Realizar una función que devuelva True si es primo y False si no lo es.

def esPrimo(num):
    for i in range (2,num):
        if(num % i==0):
            return False
    
    return True
    
num=int(input("Dime un número: "))
print(esPrimo(num))

'''
Realizar un programa que nos diga los primos que se encuentran encuentran
entre 1 y 1000
'''

def totalPrimosDe1a1000():
    for i in range(1,1001):
        if(esPrimo(i)):
            print(i)
            