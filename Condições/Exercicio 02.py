#Escreva um programa que leia a velocidade de  um carro,se ela ultrapassar 80km/h, mostre uma mensagem dizendo
#Que ele foi multado, a multa vai custar R$7.00 POR CADA KM acima da velocidade

velocidade = int(input("Digite a velocidade que o carro passou no radar:   "))
limite_de_velocidade = 80
Valor_a_ser_pago = 7.00


if velocidade > limite_de_velocidade:
   km =  velocidade - limite_de_velocidade
   valor = km*Valor_a_ser_pago

   print(f"seu carro passo no radar a {velocidade} km\h o valor da multa e {valor}")

else:
    print("Esta dentro do limite permitido")