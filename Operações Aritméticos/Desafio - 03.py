#programa mostre a media dos alunos
#entrada de dados
print("Notas de um aluno")
#entrada com float numero variado
Nota01 = float(input("Digite a nota da AV1:"))
Nota02 = float(input("Digite a nota da AV2:"))
#soma das notas informada
Soma_das_notas = Nota01+Nota02
#pega a soma e realiza divisão por 2
Media = (Soma_das_notas/2)
#saida de dados
print("Soma da AV1 {} e soma da AV2 {} e a divisão por 2 e {:.2f}".format(Nota01,Nota02,Media))


##if media >=5.0
#print("Aprovado")
#elif comment:  media >4.9
#print("Reprovador")
