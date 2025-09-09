# 4. Calculadora de Consumo de Combustível

# 1 - Solicita os dados da viagem ao usuário
# O programa pede a distância percorrida em quilômetros e o total de litros de combustível gastos.
# A função float() converte a entrada do usuário de texto para um número decimal.
distancia_percorrida = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite a quantidade de combustível gasto em litros: "))

# 2 - Realiza o cálculo do consumo médio
# O consumo médio é a razão entre a distância percorrida e o volume de combustível gasto.
# A fórmula é: km/l = distância / combustível.
consumo_medio = distancia_percorrida / combustivel_gasto

# 3 - Exibe os resultados da viagem
# Utiliza f-strings para apresentar os dados de forma clara e organizada.
# O método .2f é usado para formatar os números com duas casas decimais, ideal para medições.
print("\n--- Relatório de Consumo ---")
print(f"Distância percorrida: {distancia_percorrida:.2f} km")
print(f"Combustível gasto: {combustivel_gasto:.2f} litros")
print("----------------------------")
print(f"Consumo médio: {consumo_medio:.2f} km/l")