#Introducir un número y devolver la suma de sus digitos
#ejemplo, suma (234)=9


def suma_digitos(num):
    resultado = 0
    num_str = str(num)
    
    for i in num_str:
        resultado += int(i)
    print("Número es: ",num)
    print("Resultado: ",resultado)
    
    return resultado
    
#suma_digitos(234)

def suma_digitos1(num):
    resultado = 0
    index= 0
    num_str = str(num)
    tamanyo_str = len(num_str)
    print("Tamaño de la cadena:", tamanyo_str)

#suma_digitos1(234)
    
def suma_digitos2(num):
    resultado = 0
    
    while(num >= 10):
        resultado += (num%10)
        num = (num//10)
    resultado+= num
    print("La suma es: ",resultado)
    return resultado

suma_digitos2(234)
    