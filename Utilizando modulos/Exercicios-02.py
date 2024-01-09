#faça  um programaque leia o comprominto  do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre
#Comprimento da hipotenusa
import math
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
h1 = (co**2 + ca**2)**(1/2)
print ("A hipotenusa vai medir {:.2f}".format(h1))


co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
h1 = math.hypot(co,ca)
print ("A hipotenusa vai medir {:.2f}".format(h1))
