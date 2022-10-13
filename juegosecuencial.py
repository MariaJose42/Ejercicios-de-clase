import random

numaleatorio= random.randint(0,100)
print(numaleatorio)

num1=(int(input("Dime un número: ")))
if (num1==numaleatorio):
    print("Has ganado")
else:
    num2=(int(input("Dime otro número: ")))
    if(num2==numaleatorio):
        print("Has ganado")
    else:
        num3=(int(input("Dime un número más: ")))
        if(num3==numaleatorio):
            print("Has ganado")
        else:
            print("Has perdido")
    


    
