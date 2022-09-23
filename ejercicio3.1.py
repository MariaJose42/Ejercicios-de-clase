#Introduciendo un número en el teclado, imprimir la tabla de multiplicar
#de dicho número.

num = -1
indice = 0
resultado = -1

#Muestro mensaje

print("Dime un número: ")

num = int(input())

print("Tabla del " , num)

while(indice <= 10):
    resultado = num * indice
    print(num , " x ", indice, "=", resultado)
    indice = indice + 1
    
print("FIN")
    
    


