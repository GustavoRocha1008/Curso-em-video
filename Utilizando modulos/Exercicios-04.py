# um professor quer sortear um dos quatro alunos para apagar o quadro e faça um programa que ajude ele
# lendo  o nome deles  e escrevendo o nome do escolhido


import random
import emoji

print("Sorteio de nome: \n 01-Gustavo \n 02-Rodrigo \n 03-marcelo \n 04-Augusto \n 05-Nenhum dos alunos anteriores")
entrada01 = random.randint(1,5)
print(emoji.emojize ("\n Então o aluno sorteado e {}  :thumbs_up:".format(entrada01)))

