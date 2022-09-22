#Escriba, usando comparaciones, un algoritmo que muestre el estado del
#agua (hielo, liquido, vapor) en función de su temperatura.

temp = 0

print("Dime la temperatura del agua: ")

temp = float (input())

#Comprobamos los estados.

if( temp < 0) :
    print("El agua se encuentra en estado sólido.")
    
elif (temp >= 100) :
    print("El agua se encuentra en estado gaseoso.")
    
else : 
    print("El agua se encuentra en estado líquido.")

