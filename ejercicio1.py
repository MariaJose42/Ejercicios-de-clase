#Introduciendo la hora del día en hores,minutos y segundos, calcular cuantos
#segundos han transcurrido desde el comienzo del día.

#Definir las entradas.

hora=0
minutos=0
segundos=0

#Pedir al usuario que ingrese la hora,minutos y segundos actuales.

hora = int(input("Dime la hora:"))
minutos = int(input("Dime los minutos:"))
segundos = int(input("Dime los minutos:"))

#Realizamos la operacion.

hora = hora * 3600
minutos = minutos * 60
segundos = segundos + minutos + hora

#Mostramos los resultados

print("Han pasado desde el inicio del día ", segundos, "segundos.")