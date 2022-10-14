'''
Definir una función que devuelva una
lista con 20 números random
'''
# lista_numeros()
# devuelve por ejemplo ---> [2,4,3,4,5,17,3,4,7,9,10,12,15,16,18,29,98,87,65,30]
# len(lista_numeros()) --> 20
# type(lista_numeros)) --> <class 'list'>

import random

def lista_numeros():
    lst=[]
    for i in range (0,20):
        lst.append(random.randint(0,100))
    return lst
        
#print(lista_numeros())

'''
Definir una función que dado una lista
filtre los números pares
'''
# filtra_lista_pares([1,2,3,4])
# devuelve ---> [2,4]

lst1=lista_numeros()
#print(lst1)

def filtra_lista_pares(lst1):
    lst2=[]
    for i in lst1:
        if(i%2==0):
            lst2.append(i)
    return lst2

#print(filtra_lista_pares(lst1))


'''
Definir una función que dado una lista y un número
devuelva
   - True si se encuentra el número en la lista
   - False e.c.c.
'''

lst1=[1,2,3]
lista_numeros()
num=2
random.randint(0,100)
print(num)
print(lst1)

def busqueda_num(lst,num):
    for i in lst1:
        if(i==num):
            return True
        else:
            return False
        
print(busqueda_num(lst1,num))
      