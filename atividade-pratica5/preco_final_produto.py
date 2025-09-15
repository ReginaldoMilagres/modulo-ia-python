def calcular_preco_com_desconto():
    """
    Calcula o preço final de um produto após a aplicação de um desconto percentual.
    Solicita o preço original e a porcentagem de desconto ao usuário.
    """
    print("--- Calculadora de Desconto ---")
    
    try:
        # a - Interação com o usuário: Pede os valores necessários
        preco_original = float(input("Digite o preço original do produto: R$ "))
        porcentagem_desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))
        
        # b - Cálculo do desconto
        valor_desconto = preco_original * (porcentagem_desconto / 100)
        
        # c - Preço final
        preco_final = preco_original - valor_desconto
        
        # d - Formatação: Arredonda o resultado para 2 casas decimais
        valor_desconto_formatado = round(valor_desconto, 2)
        preco_final_formatado = round(preco_final, 2)
        
        # e - Interação com o usuário: Mostra o resultado formatado
        print("\n--- Resultado ---")
        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto aplicado: R$ {valor_desconto_formatado:.2f}")
        print(f"Preço final com desconto: R$ {preco_final_formatado:.2f}")
    
    except ValueError:
        print("\nErro: Por favor, digite apenas números válidos para o preço e o desconto.")

# Executa a função
calcular_preco_com_desconto()