#Faça um programa que leia uma frase pelo o teclado e mostra:
#Quantas vezes aparece a letra "A" - ok 
#Em que posição ela aparece a primeira vez 
#Em que posição ela aparece a ultima vez.

leia = input ("Digite uma palavra: ")
#lower converte tudo para minúsculas para garanti que a contagem seja certa
frase = leia.lower()
#count ira conta quantas letras deseja tem 
texto = leia.count ("a")
#find  encontra a letra deseja e o +1 e para começar do 1 vez do zero conforme e o python
texto1 = leia.find("a") +1 
#rfind começa da esquerda para a direita 
texto2 = leia.rfind("a") 
#f e para poder colocar valor variado dentro da string
print (f"Quantas vezes aparece a letra A e {texto} ")
print (f"Em que posição ela aparece a primeira vez em {texto1}")
print (f"Em que posição ela aparece a ultima vez em {texto2}")