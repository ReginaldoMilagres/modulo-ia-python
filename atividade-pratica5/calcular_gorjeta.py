def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta e o valor total da conta, incluindo a gorjeta.

    Parâmetros:
    - valor_conta (float): O valor total da conta antes da gorjeta.
    - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%).

    Retorna:
    - tuple: Uma tupla contendo o valor da gorjeta e o valor total final da conta.
             Ex: (valor_gorjeta, valor_total_final)
    """
    # Converte a porcentagem para um valor decimal
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    
    # Calcula o valor total da conta com a gorjeta
    valor_total = valor_conta + gorjeta
    
    # Retorna o valor da gorjeta e o valor total, formatados para duas casas decimais
    return round(gorjeta, 2), round(valor_total, 2)

# --- Exemplo de uso da função ---
try:
    # Solicita a entrada do usuário para o valor da conta e a porcentagem da gorjeta
    valor_da_conta_input = float(input("Digite o valor total da conta: "))
    porcentagem_da_gorjeta_input = float(input("Digite a porcentagem de gorjeta desejada (ex: 15): "))
    
    # Chama a função para obter os valores
    valor_da_gorjeta, valor_total_final = calcular_gorjeta(valor_da_conta_input, porcentagem_da_gorjeta_input)
    
    # Exibe os resultados para o usuário
    print(f"\n--- Detalhes da Conta ---")
    print(f"Valor da conta: R$ {valor_da_conta_input:.2f}")
    print(f"Porcentagem da gorjeta: {porcentagem_da_gorjeta_input:.2f}%")
    print("-------------------------")
    print(f"Valor da gorjeta: R$ {valor_da_gorjeta:.2f}")
    print(f"Valor total a ser pago: R$ {valor_total_final:.2f}")

except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")