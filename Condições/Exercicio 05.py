#Faça um proma que leia um ano qualquer e mostre se ela é BISSEXTO
Number = int(input("Digite o ano desejado:    "))
bixesto = 4
nao_bixesto = 100 

if Number <= bixesto:
   divisao =  bixesto % 4 ==0
   print(f"{divisao} e então o ano e bixesto")

else:
   divisao1 = nao_bixesto % 100 == 300
   print (f"o ano informado foi {Number} e o resultado deu que o ano não e bixeto")
