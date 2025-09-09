# 2. Calculadora de Desconto

# 1 - Recebe as informações do produto e do desconto a partir da entrada do usuário
# A função input() lê a entrada do teclado, e float() converte o texto para um número decimal.
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original do produto (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# 2 - Converte a porcentagem de desconto para um valor decimal
# Para realizar o cálculo, a porcentagem precisa ser convertida de 0-100 para 0-1.
desconto_decimal = porcentagem_desconto / 100

# 3 - Calcula o valor do desconto
# O valor do desconto é encontrado multiplicando o preço original pela taxa decimal.
valor_desconto = preco_original * desconto_decimal

# 4 - Calcula o preço final
# O preço final é o resultado da subtração do valor do desconto do preço original.
preco_final = preco_original - valor_desconto

# 5 - Exibe os resultados
# Usamos f-strings para apresentar os valores de forma clara e arredondada para duas casas decimais,
# o que é ideal para valores monetários.
print("\n--- Detalhes do Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto:.2f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print("----------------------------")
print(f"Preço final: R$ {preco_final:.2f}")