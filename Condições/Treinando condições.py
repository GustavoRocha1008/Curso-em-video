
#Condições de nome- estrutura Condicional composta
Inserir_nome = str(input("Qual e seu nome: "))
nome = Inserir_nome.upper()
if nome == "GUSTAVO":
    print ("Verdade")
else:
    print ("Para de mentir!")
print ("E isso!")



#condições de notas - estrutura condicional composta 
Inserir_notas = int(input("Digite sua nota: "))
if Inserir_notas >=5:
    print( "Parabens aprovado")
else: 
    print("Reprovado")
print("\n Otimas ferias!")



#Condições de bom dia! e uma estrutura condicional simples 
identificacao = str(input("Qual e o modelo do seu carro: "))
if identificacao == "Nivus":
    print ("Nivus e um otimo carro")
print ("Otimo modelo o seu {} parabens" .format(identificacao))

