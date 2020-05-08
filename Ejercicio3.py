# Confeccionar un programa que permita cargar un número entero positivo de hasta
#  tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
# Mostrar un mensaje de error si el número de cifras es mayor.
a=int(input('Valor 1: '))
if a<10:
    print('1 cifra')
elif a>=10 and a<100:
    print('2 cifra')
else:
    print('3 cifra')