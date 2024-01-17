#Aluguel de carro
Valor = float (input("Qual e o valor do produto:"))
#pega o valor e faz x 5
calculo = Valor * 5
#divide o valor /100
Calculo1 = calculo/100
#faz a subtração 
Calculo2 = Valor - Calculo1
#Saida mostrando valor do produto e o quanto ele ficou com desconto 
print("Então o valor do produto e {} e com o desconto ele ficou {}".format(Valor,Calculo2))

#Outra forma de fazer
Valor =float(input("Qual e o valor do produto:"))
calculo = Valor-(Valor*5/100)
print("Então valor do produto e R${} então o valor total com desconto e: R${}".format(Valor,calculo))
