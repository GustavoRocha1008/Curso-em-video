#Desenvolva um programa que pergunta a distancia de uma viagem em KM. Calcule o preço da passagem
#R$ 0.50 por km para viagens de até 200Km a R$0.45 para viagens mais longas

entrada = float(input("Quantos KM voce rodo:  "))
viagem_Longa_ate_200km= 0.50  
viagem_Longa_alem_200km = 0.45 
limit_km = 200

if entrada  <= limit_km:
    valor_curto =viagem_Longa_ate_200km * entrada
    print(f"voce rodou {entrada}km a passagem por KM ficou {valor_curto:.2f}")

else:   
    valor_longo =viagem_Longa_alem_200km * entrada
    print(f"voce rodou {entrada}km a passagem por KM ficou {valor_longo:.2f}")



