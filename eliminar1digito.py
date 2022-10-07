'''
Realizar un programa que:
"Dado un número eliminar su primer digito."
'''

num= input("Dime un número:")
tam= len(num)

num_sin_digito=""


for i in range(1,tam):
        num_sin_digito+=num[i]
        
print(num_sin_digito)