#Aluguel de carro - primeira opção
Entrada01 = int(input("Quantos dias o carro esta alugado:"))
Entrada02 = float(input("Quantos Km rodou:"))
Calculo   = Entrada01 * 60
Calculo2  = Entrada02 * 0.15
Calculo3  = Calculo + Calculo2
print("Então o carro ficou alugado por {} dias e rodou {} Km então o valor a ser pago e R${:.2f}".format(Entrada01,Entrada02,Calculo3))

#Outra opção para realizar o programa 
Dias = int(input("Dias que o carro esta alugado:"))
Km   = float(input("Km rodados nesse periodo:"))
Calculo =(Dias * 60) + (Km * 0.15)
print("Total a ser pago:",Calculo)