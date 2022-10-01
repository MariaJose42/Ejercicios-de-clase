#Dados dos números , decir cual es mayor y cual menor.

def mayor_menor(a,b):
    pass

# Realizamos la función

def mayor_menor(a,b) :
    if (a>b):
        print("a:", a,"es mayor que b:",b)
    else:
        print("b:", b,"es mayor que a:",a)
                
#mayor_menor(3,4)
#mayor_menor(4,3)
    
#Programa me diga el mayor y el menor de tres números.
        
def mayor_menor_3(a,b,c):
    if(a>b and a>c):
        print("a:", a,"es el mayor" )
        if(b>c):
            print("c:", c,"es el menor" )
        else:
            print("b:", b,"es el menor")
            
    if(b>a and b>c):
        print("b:", b,"es el mayor" )
        if(a>c):
            print("c:", c,"es el menor" )
        else:
            print("a:", a,"es el menor")
            
    if(c>b and c>a):
        print("c:", c,"es el mayor" )
        if(a>b):
            print("b:", b,"es el menor" )
        else:
            print("a:", a,"es el menor")
            
        
        
#mayor_menor_3(1,2,3)
#mayor_menor_3(3,2,1)
#mayor_menor_3(1,3,2)

#Programa que intercambia los valores de entrada.
def intercambia(a,b):
    (a,b) = (b,a)
    print((a,b))
    
intercambia(1,2)
intercambia(4,5)