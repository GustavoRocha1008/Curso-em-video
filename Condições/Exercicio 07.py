#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário
#se ela podem ou não formar um triangulo
print("-=-"*40)
R1 = float(input("Digite a primeira reta:  "))
R2 = float(input("Digite a segunda  reta:  "))
R3 = float(input("Digite a terceira reta:  "))
print("-=-"*40)

if R1 < R2 + R3 and R2 < R1 + R3 and R3 < R1 + R2:
    print("forma um triangulo")

else:
    print("não forma um triangulo")