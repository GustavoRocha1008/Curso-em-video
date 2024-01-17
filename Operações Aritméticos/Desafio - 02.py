#Scripty  crie  algoritmo que leia um numero e mostra o seu dobro triplo e raiz quadrado 
#mostra mensagem para o cliente
print("Good morning")
#Entrada de dados 
Number = int(input("Digite o valor desejado abaixo:"))
#calcula o dobro
Calculo = Number * 2
#calculo o triplo
Calculo02 = Number * 3
#calculo a raiz quadrada
Calculo03 = Number ** (1/2)
#mensagem de saida formatada em .format
print("Valor do calculo é:{} e o triplo {} e a raiz e {:.3f}".format(Calculo,Calculo02,Calculo03))
