#Escreva um programa que pergunta o salario de um funcionario e calcule o valor do seu aumento,
#Para salarios superiores a R$ 1.250,00. calcule um aumento de 10%
#para os inferiores ou iguais o aumento é de 15%

entrada = float(input(" Digite o valor do seu salario:"))
salario_base = 1250.00
maior = 0.10
menor = 0.15

if entrada >= salario_base:
    calculo = entrada + entrada * maior
    print (f"O salario informado e de {entrada} o aumento e de 10% o total do aumento e {calculo}")

else: 
    calculo1 = entrada + entrada * menor
    print (f"o  salario informado e de {entrada} o aumento e de 15% o total do aumento e {calculo1}")
