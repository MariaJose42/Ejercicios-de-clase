def factorial_while(num):
    #Inicializo las variables
    res=1
    while(num >= 1):
        res= res*num
        num=num-1
    return res


def factorial_for(num):
    res=1
    for i in range (1,num+1):
        res=res*i
    return res


def factorial_rec(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return n*factorial_rec(n-1)


import time

inicio=time.time()
factorial_while(30)
fin=time.time()
total= fin-inicio

print("El programa factorial_while ha tartado ",total,"segundos.")



inicio=time.time()
factorial_for(30)
fin=time.time()
total= fin-inicio

print("El programa factorial_for ha tartado ",total,"segundos.")



inicio=time.time()
factorial_rec(30)
fin=time.time()
total= fin-inicio

print("El programa factorial_rec ha tartado ",total,"segundos.")