#Escriba un algoritmo que determine la categoría deportiva de un usuario
#en función de su edad.
''' - 6 a 7 años: benjamin
    - 8 a 9 años:  alevín
    - 10 a 11 años: infantil
    - 12 años y más: cadete
'''

edad= 0

print ("Dime tu edad : ")

edad = int(input())

if (6<=edad<=7) :
    print("Eres benjamín")
    
elif (8<=edad<=9):
    print("Eres alevín")
    
elif (10<=edad<=11):
    print("Eres infantil")
    
else:
    print("Eres cadete")