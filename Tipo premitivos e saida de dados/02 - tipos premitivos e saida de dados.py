# Tipos primitivos e saida de dados #
#int - valor inteiro, (7 -4 0 9875)
#float -numeros reais (4,5 0.076 -15.223 7.0)
#bool- valores logicos e boleanos (True e False)
#str - valores caracteres e stri ('Ola' '7.5' '')



fatura01 = int(input('Digita o valor da fatura:'))
fatura02 = int(input('Digita o valor da segunda fatura:'))

print('Então esse e o valor:', fatura01 + fatura02,)

Fatura03 = float(input('Digita o valor quebrado da fatura:'))
Fatura04 = float(input('Digita o valor quebrado da fatura:'))

print('Então esse e o valor quebrado:', Fatura03 + Fatura04)

Fatura05 = int(input('Digite o valor: '))
Fatura06 = int(input('Digite o valor: '))
Calculo = Fatura05 + Fatura06
# forma de mostrar o valor de forma diferente e o formato antigo do python
#print('então soma entre',Fatura05,'e',Fatura06, 'vale' , Calculo)
#formato mais novo do python
print('então soma entre {} e {} vale {}'.format(Fatura05,Fatura06,Calculo))
      