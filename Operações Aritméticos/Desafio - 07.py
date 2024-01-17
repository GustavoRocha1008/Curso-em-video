#Entrada
larg = float(input("Digite a largura da parede:"))
Alt  = float(input("Digite a altura da parade:"))
#calcula faz largua x altura
Calculo = larg*Alt
#calculo1 faz a divisão por dois
calculo1 = Calculo/2
#Sainda foamartada e ponto format!
print("Então a largura da parede e {} e altura {}m²e quantidade de tinta a ser utilizada {:.22f}l" .format(larg,Alt,calculo1))
