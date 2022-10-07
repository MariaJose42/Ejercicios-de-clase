#Factorial Ejemplo: 4!=4*3*2*1=24
#Realizar un programa que calcule el Factorial de un número
'''
def factorial(num):
    #Inicializo las variables
    res=1
    while(num >= 1):
        res= res*num
        num=num-1
    return res

print("Factorial es: ",factorial(4))'''


def factorial_for(num):
    res=1
    for i in range (1,num+1):
        res=res*i
    return res
    
print("Factorial es: ",factorial_for(4))