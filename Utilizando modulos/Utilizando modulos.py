#Tem duas maneiras de realiazação de realização de importa biblioteca em python com o import antes de tudo e ou com o from""import
#biblioteca math
#Ceil - Arredondamento para cim 
#flor - arrendondamento para baixa
#Trunc - so vale da virgula para frente
#pow - pontencia
#sqrp - raiz quadrada
#factorial
import math
entrada01 = int(input("Digite um numero:"))
calculo = math.sqrt(entrada01)
print("A raiz quadrada de {} e {}".format(entrada01,math.trunc(calculo)))

Entrada02 = int(input("Digite um numero:"))
Calculo02 = math.sqrt(Entrada02)
print("A raiz quadrada de {} e {}".format(Entrada02,math.trunc(Calculo02)))


Entrada03 = float(input("Digite um numero:"))
calculo3 = math.floor(Entrada03)
print("Então o numero {} arredondado para baixo e {}" .format(Entrada03,math.floor(calculo3)))

