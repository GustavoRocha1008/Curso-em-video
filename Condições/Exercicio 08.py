info1 = float(input("Digite o primeiro numero: "))
info2 = float(input("Digite o segundo numero: "))
info3 = float(input("Digite o terceiro numero: "))

# Inicializando as variáveis para armazenar o maior e o menor número
maior_numero = menor_numero = info1

# Verificando o segundo número
if info2 > maior_numero:
    maior_numero = info2
elif info2 < menor_numero:
    menor_numero = info2

# Verificando o terceiro número
if info3 > maior_numero:
    maior_numero = info3
elif info3 < menor_numero:
    menor_numero = info3

# Exibindo os resultados
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
