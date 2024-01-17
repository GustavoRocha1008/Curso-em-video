#print('Boa tarde')
#Digite = bool(input('Digite o valor: '))
#print (type(Digite),(Digite))

#print('Boa tarde')
#Digite = bool(input('Digite o valor: '))
#print(type(Digite))

#interação com usuário
print('Boa tarde')
#Interação de entrada de dados 
Digite = input('Digite algo:')
#saida formatada com isnumeric método issnumeric () retorna “True” se todos os caracteres da string forem numéricos, caso contrário, retorna “False”.
print('valor e numerico:', Digite.isnumeric())
#saida formatada com Esta função é usada para verificar se o argumento inclui apenas caracteres do alfabeto (mencionados abaixo).
print('e alphabetico:',Digite.isalpha())
#saida formatada com isspace um método embutido usado para manipulação de strings. O método isspace () retorna “True” se todos os caracteres da string forem espaços em branco, caso contrário, retorna “False”
print('Tem espaço', Digite.isspace())
#saida formatada com escrição o istitle()O método verifica se todos os caracteres baseados em maiúsculas e minúsculas na string após as letras não casadas estão em maiúsculas e todos os outros caracteres baseados em maiúsculas estão em minúsculas.
print("Tem letra maiuscula", Digite.istitle())
#saida formatada com  isdecimal e uma função em Python que retorna verdadeiro se todos os caracteres em uma string forem decimais.
print ('Tem letra minusculo', Digite.isdecimal())