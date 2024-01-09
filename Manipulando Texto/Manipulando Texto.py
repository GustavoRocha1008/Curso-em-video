#frase = curso em video pyhton 
#Fatiamento [] - o ultimo valor não entra na contagem 
#Frase [:5] - ele não mostra aonde vai começar e começa do zero e vai te o 5
#Frase [5:] - ele começa no 5 porem ele vai ate o final 
#Frase [5::3] - ele iria começar no 5 e pularia de 3 ate o final da string
#Analise - len(Frase)
#frase.count('o') - Contas quantas vezes aparece a letra O 
#frase.count('0',0,13) - Conta quantas letra O tem no codigo fatiando em 3
#frase.find('deo') - Aonde inicia a palavra 
#Transformação - frase.replace ('python','Android') - ele vai procura por python e substitur por android
#frase.upper() - letras minuscula ele joga para maiscula
#frase.lower() - Mantem o que minusculo e substitui os maiusculo para minusculo
#frase.capitalize() - tudo para minusculo e so primeiro fica em maiusculo 
#frase.title() - Ele vai analisar quantas palavras ele tem (Contado pelos espaço)
#frase.strip() -  vai remover os primeiros espaço e o ultimos
#frase.rstrip() - o R e para ele começa a trata pela a direita( ele remove sommente os ultimos espaço)
#frase.Istrip() - o I e para ele comecar a retira os espaço da esquerda
#frase.split() - para cada palavra ele gera uma lista
#Junção - '-'.join(frase)

frase = ("Curso em Video Python")
divido = frase.split()
print(frase)
print(frase[1])
print(frase[1:4])
print(frase[1:15:2])
print (frase.count('o'))
print(frase.upper().count('V'))
print(len(frase))
print(frase.replace('Python','Java'))
print('curso' in frase)
print('Curso' in frase)
print(divido[0])