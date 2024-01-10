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