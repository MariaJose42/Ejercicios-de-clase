#Realizar un programa que sea capaz de convertir los grados
#centígrados en grados Farenheit y viceversa.

#Definir las entradas.

celsius = 0
farenheit = 0

#Pedir al usuario que ingrese los grados celsius.

celsius = float(input("Dime los grados celsius:"))

#Realizamos la operacion.

farenheit = 1.8 * celsius + 32

#Mostramos los resultados

print(celsius, " grados centigrados son ", farenheit, "grados farenheit.")
