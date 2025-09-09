# 1. Conversor de Moeda

# Define as taxas de câmbio (é importante manter esses valores atualizados)
taxa_dolar = 5.25  # Taxa de conversão de R$ para Dólar (exemplo)
taxa_euro = 5.60   # Taxa de conversão de R$ para Euro (exemplo)

# Solicita o valor em reais ao usuário
valor_reais = float(input("Digite o valor em reais (R$): "))

# Calcula a conversão para dólar
# O valor em reais é dividido pela taxa do dólar para obter o valor equivalente em dólares.
valor_dolar = valor_reais / taxa_dolar

# Calcula a conversão para euro
# O valor em reais é dividido pela taxa do euro para obter o valor equivalente em euros.
valor_euro = valor_reais / taxa_euro

# Exibe os resultados formatados
# Usamos f-strings para formatar o texto e o método .2f para arredondar
# os valores convertidos para duas casas decimais, o que é ideal para moedas.
print(f"O valor de R$ {valor_reais:.2f} equivale a:")
print(f"US$ {valor_dolar:.2f} dólares.")
print(f"€ {valor_euro:.2f} euros.")