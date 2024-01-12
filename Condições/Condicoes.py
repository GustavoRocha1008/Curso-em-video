#Condições - GRANDE MAIORIA DOS PROGRAMAS TEM AS CONDIÇÕES
#Estrutura sequencia - ela feita de uma sequencia

#condições em python e: if (dentro a descrição): (bloco verdadeira (True))
#condições em python e  else: (Bloco falso)
#nunca sera executado dois bloco ao mesmo tempo 
#todo comando que esta do lado esquerdo sera executado porem, quando esta endentado ele depende da condição para executar
tempo = int(input('Quanto tempo tem seu carro? '))

if tempo <=2:
    print ("Carro novo")
else:
    print ("Uma bosta!")
    print ("--Boa sorte--")

#Condição simplicada com format
tempo1 = int(input("Quanto tempo tem seu veiculo?:  "))
print('Carro novo' if tempo1 <=1  else "Carro velho com {} anos".format(tempo1))
print("Boa sorte!")

#condição simplificada com f 
tempo2 = int(input("Quanto tempo tem seu veiculo?: "))
print(f"Carro novo" if tempo1 <= 1 else f"Carro velho, com {tempo1} anos")
print("Boa sorte!")
