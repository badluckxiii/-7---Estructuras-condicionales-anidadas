# Se ingresa por teclado un valor entero, mostrar una leyenda que 
# indique si el número es positivo, negativo o nulo (es decir cero)
a=int(input('Valor 1: '))
if a<0:
    print('Negativo')
elif a==0:
    print('Nulo')
else:
    print('postivo')