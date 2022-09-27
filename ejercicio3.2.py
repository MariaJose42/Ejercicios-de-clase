#Introduciendo un número en el teclado de ordenador, hallar cuantos
#números enteros múltiplos de tres, hay comprendidos entre la unidad y dicho
#número.

num = -1
total_multiplos = 0
indice = 1

#Pregunto al usuario el número.
num = int(input ("Dime un número: "))

while (indice<=num):
    if(indice%3==0):
        total_multiplos += 1 #total_multiplos = total_multiplos + 1
    indice = indice + 1

print ("Entre la unidad y",num,"hay un total de",total_multiplos,"números multiplos de 3.")

