#Mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

Nome1 = input("Digte o primeiro nome:")
Nome2 = input("Digte o segundo nome:")
Nome3 = input("Digte o terceiro nome:")
Nome4 = input ("Digite o quarto nome:")

lista = (Nome1,Nome2,Nome3,Nome4)
sorteio = random.choice(lista)
print('o nome escolhido foi:', sorteio)



print('\n Boa tarde')
n1 = str (input('Digite o primeiro nome:    '))
n2 = str (input('Digite o segundo  nome:    '))
n3 = str (input('Digite o terceiro nome:    '))
n4 = str (input('Digite o quarto   nome:    '))
lista =  [n1, n2, n3, n4]
random.shuffle  (lista)
print    ('Nova ordem é:\n ')
print    (lista)



from random import shuffle
n1 = str(input(" \nDigite o primeiro nome:   "))
n2 = str(input("Digite o segundo nome:       "))
n3 = str(input("digite o terceiro nome:      "))
n4 = str(input("Digite o quarto nome:        "))
lista = [n1,n2,n3,n4]
shuffle(lista)
print (lista)