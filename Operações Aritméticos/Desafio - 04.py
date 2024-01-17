#Programa - Escreva um programa que leia o valor em metros e a exiba convertido em centimetrosa milimetros
#Mensagem de entrada
print("Bom dia")
#entrada de dados floot
Number01 = float(input("Digite quantos metros tem?"))
# faz a conversão para milimetro
m = Number01*100
# faz conversão apra centimetro
cm = Number01*1000
#saida de dado com .format
print("Então {}metros tem em centimento e {} e milimetros e {}".format(Number01,m,cm))
