import math 
lado= float(input("Ingrese el valor del lado del triangulo equilatero.  "))
area= math.sqrt(3/4) * (lado*lado)
print("el area del triangulo es:", area)
if area > 1000:
 print("el area es mayor a 1000")