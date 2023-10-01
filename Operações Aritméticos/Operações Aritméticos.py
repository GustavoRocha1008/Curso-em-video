#Adição = +
#Subtração = -
#Multiplicação = *
#Divisão = /
#Potencia = **
#Divisão inteira =//
#Resto da divisão = %
#Ordem de precedencia 
#()
#**
#*/ // %
#+ -
# quebra de linha \n
#Continuar na mesma linha end= ''.

Entrada = int(input('Digite o valor:'))
Entrada01 = int(input('Digite o valor:'))
Calculo = Entrada+Entrada01
CalculoSubtração = Entrada-Entrada01
CalculoMultiplicação = (Entrada*Entrada01)
CalculoDivisão = (Entrada/Entrada01)
CalculoPotencia = (Entrada//Entrada01)
CalculoRestodivisao = (Entrada%Entrada01)

print("Então o valor da \n somatario:{} \n subtração:{} \n multiplicação:{} \n Divisão:{:.3f}".format(Calculo,CalculoSubtração,CalculoMultiplicação,CalculoDivisão), end='')
print("\n Potencia {} \n Resto da divisão {}".format(CalculoPotencia,CalculoRestodivisao))

print("\nTeste Dois")
Entrada02 = int(input("Entrada de dado:"))
Entrada03 = int(input("Entrada de dados:"))
Calculo4 = Entrada02-Entrada03      
Calculo2  = Calculo4*2
print("então valor e {} e o valor e {}".format(Calculo4,Calculo2))

