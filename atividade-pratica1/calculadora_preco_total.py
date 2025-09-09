# Esse programa calcula o preço total de uma compra
 
# Solicita informações  sobre o produto ao usuário
nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o Preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

# Calcula preço total
preco_total = preco_unitario * quantidade

# Exibe preço total
print(f"\nNome do produto: {nome_produto}")
print(f"Preço_unitário: {preco_unitario}")
print(f"Quantidade: {quantidade}")
print(f"Total: R${preco_total:.2f}")