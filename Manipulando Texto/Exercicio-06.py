#Faça um programa que leia o nome completo de uma pessoa,mostre en seguida o primeiro e o ultimo nome separadamente
#ex: Ana maria de souza
#primeiro:Ana 
#Ultimo:Souza
nome_completo = input("Digite seu nome completo: ").strip()
partes_do_nome = nome_completo.split()

primeiro_nome = partes_do_nome[0]
ultimo_nome = partes_do_nome[-1]

print("Primeiro nome: {}".format(primeiro_nome))
print("Último nome: {}".format(ultimo_nome))