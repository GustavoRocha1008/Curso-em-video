#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#Ex: digite um número: 1834
#unidade:4
#dezena:3
#centena:8
#milhar:1

inserir = str(input("Informe um numero:"))
number = str(inserir)
print("Analisando um numero: {}" .format(inserir))
print("A unidade de {} e {}". format(inserir, number[3]))
print("A dezena  de {} e {}". format(inserir, number[2]))
print("A centena de {} e {}". format(inserir, number[1]))
print("O milhar  de {} e {}". format(inserir, number[0]))
print('\n')


inserir1 = int(input("Informe um numero:"))
U =  inserir1 // 1 % 10
d =  inserir1// 10 % 10
c =  inserir1//100 % 10
m =  inserir1//1000% 10


print("Analisando um numero: {}" .format(inserir1))
print("A unidade e: {}".format(U))
print("A dezena  e: {}".format(d))
print("O centena e: {}".format(c))
print("O milhar  e: {}".format(m))
