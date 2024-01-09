Salario = float(input("Digite o valor do salario do funcionario:"))
Base_de_calculo = Salario  + (Salario*15/100) 
print("O seu antigo salario era R${:.3f} e com reajuste de 15% ficou R${:.3f}".format(Salario,Base_de_calculo))
