#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculo - ok
#O nome com todos minusculo ok
#quantas letras ao todo(Sem considerar espaço)ok
#Quantas letras tem o primeiro nome ok


#Crie um programa que leia o nome completo de uma pessoa e mostre:
Digite = input ("Digite seu nome:  \n")
#O nome com todas as letras maiusculo -
maiusculo = Digite.upper ()
#O nome com todos minusculo 
minusculo = Digite.lower ()
#quantas letras ao todo(Sem considerar espaço)
espaco = len(Digite.replace(" "," "))
#Quantas letras tem o primeiro nome
letras = Digite.split()
letras1 = letras[0]
letras2 = len(letras1)

print (f"O nome com todas as letras maiusculo: {maiusculo}")
print (f"O nome com todos minusculo: {minusculo}")
print (f"quantas letras ao todo(Sem considerar espaço): {espaco}")
print (f"Quantas letras tem o primeiro nome: {letras2}")


#Str ela ja entra como string , e o strip ja na entrada cortando as informações sem o espaço 
entrada = str( input("Digite seu nome: \n")).strip()
#aqui utilizamos  o .format para inserir dados na frase o upper transformado para maiusculo 
print ("Então seu nome todo maiusculo e : {}". format(entrada.upper()))
#aqui utilizamos  o .format para inserir dados na frase o lower transformado para minusculo 
print ("Então seu nome minusculo e : {}"   .format(entrada.lower()))
#aqui utilizamos  o .format para inserir dados na frase a função len para conta as palvras, o entrada.count e para conta os espaço e fazer - len para da o resultado correto
print ("Então quantas letras seu nome tem : {}".format(len(entrada) -entrada.count(' ')))
#Quantas letras tem o primeiro nome
separa = entrada.split ()
print("então seu primeironome e: {} e tem tantas letras: {}".format(separa[0], len(separa[0])))