#Faça  um programa que leia um angulo qualquer e mostre na tela o  valor  do seno,cosseno  e tangente desse angulo
import math
angulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(angulo))
print("Angulo de {} tem seno de {:.2f}".format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem cosseno de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo,tangente))
