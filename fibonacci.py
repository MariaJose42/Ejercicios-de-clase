#Crear una función cuyo parámetro de entrada sea la posición de
#Fibonacci

def fib(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(5))