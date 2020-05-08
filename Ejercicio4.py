#  Un postulante a un empleo, realiza un test de capacitación, se obtuvo 
# la siguiente información: cantidad total de preguntas que se le realizaron y la
#  cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa 
# que ingrese los dos datos por teclado e informe el nivel del mismo según el 
# porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
# 	Nivel máximo:	Porcentaje>=90%.
# 	Nivel medio:	Porcentaje>=75% y <90%.
# 	Nivel regular:	Porcentaje>=50% y <75%.
# 	Fuera de nivel:	Porcentaje<50%.
a=int(input('Valor 1:'))
b=int(input('Valor 2:'))
if(a>=9 and b>=9):
    print('Nivel máximo')
elif a>=7 and b>=7:
    print('Nivel medio')
elif a>=5 and b>=5:
    print('Nivel regular')
else:
    print('Fuera de nivel')