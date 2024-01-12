#escreva um programa que leia o nome de uma pesssoa e diga se  ela tem "SILVA" no nome.

#Entrada do programa
Entrada01 = input("Digite seu nome completo: \n")
#Pega os dados de entra e converte tudo para minusculo
entrada02 = Entrada01.lower()
#Mostra o silva esta presenta na informação que foi inserida
print ("silva" in entrada02 )

nome = str(input("Digite seu nome:  \n"))
print(nome[:5].upper()=='SILVA')