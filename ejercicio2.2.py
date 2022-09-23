#Escriba un algoritmo que determine la categoría deportiva de un usuario
#en función de su edad.
''' - 6 a 7 años: benjamin
    - 8 a 9 años:  alevín
    - 10 a 11 años: infantil
    - 12 años y más: cadete
'''

edad= 0

print ("Dime la edad del niño: ")

edad = int(input())

if (edad<6):
    print("No tiene categoría")

elif (6<=edad<=7) :
    print("Es benjamín")
    
elif (8<=edad<=9):
    print("Es alevín")
    
elif (10<=edad<=11):
    print("Es infantil")
    
else:
    print("Es cadete")

