#crie um programa que leia o nome de  uma cidade e diga se ela começa ou não com o nome "Santo".
#entrada01 = Identificacao.lower().startswith("Santos")

#Entrada de dados
Identificacao = input("Qual e o nome da sua cidade:   ")
#verifica se o nome da cidade começa com "santos" (ignorando maiúsculas e minúsculas)
codigo = Identificacao.lower().startswith("santos")
#Saida da informação o F ele permite coloca valor dentro da string
print (f"A cidade começa com santos: {codigo}")