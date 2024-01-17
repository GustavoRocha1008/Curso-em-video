#Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5 e peça a o usuário descobri
#qual foi o  numero escolhido pelo o computador,O programa devera escrever na tela seu o usuário vencu ou perdeu

from random  import randint
from time import sleep
Computador  = randint(0,3 )# faz o computador pensar 

print ('-=-'*10)
jogador = int(input("Em qual numero estou pensando de 0 ao 3:     ")) #Jogador tentar adivinhar 
print ('-=-'*10)

print("PROCESSANDO")
sleep(5)#fUNÇÃO PARA SIMULAR A PROCESSAMENTO DE DADOS 

if jogador == Computador: # condições se o usuário acerta
    print ("Parabens voce acertou o numero e {}".format (Computador))


else: # condição se o usuário perde
    print("Desculpa voce errou o numero que digitou foi {} e o que pensei e {}" . format(jogador,Computador))