#Converso de de real para dolar e euro 
entrada = float(input("Digite quanto dinheiro voce tem na carteira?  R$"))
Dolar = entrada / 5.17
Euro  = entrada / 5.45
print ("Então você tem em R${:.2f} e conseguira comprar com a cotação atual US${:.2f}".format(entrada,Dolar))
print ("Então você tem em R${:.2f} e conseguiria comprar a cotação atual {:.2f}".format(entrada,Euro))