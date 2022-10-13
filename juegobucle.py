import random

numAleatorio = random.randint(0,100)
vidas = 3
print(numAleatorio)
while(vidas > 0):
    numUsuario = int(input("Dime un número: "))
    if(numUsuario != numAleatorio):
        vidas = vidas - 1
        
        if(vidas != 1):
            print("Te quedan ", vidas, " oportunidades.")
        else:
            print("Te queda ", vidas, " oportunidad.")
        
    else:
        print("Has acertado el número.")
        break
if(vidas == 0):
    print("El número era ", numAleatorio)