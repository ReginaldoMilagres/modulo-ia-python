def contar_pares_impares():
    """
    Analisa e classifica números como pares ou ímpares,
    e contabiliza o total de cada tipo.
    """
    print("--- Analisador de Números Pares e Ímpares ---")
    print("Digite um número por vez ou 'fim' para o resultado.")

    # Variáveis para armazenar a contagem
    contagem_pares = 0
    contagem_impares = 0

    while True:
        entrada = input("Digite um número: ")

        # Condição de saída do loop
        if entrada.lower() == 'fim':
            break

        try:
            # Converte a entrada do usuário para um número inteiro
            numero = int(entrada)

            # Usa o operador de módulo (%) para verificar se o número é par ou ímpar
            # Um número é par se o resto da divisão por 2 for 0
            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                contagem_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                contagem_impares += 1
            
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
        
        print("---")

    # Exibe o resultado final após o loop ser encerrado
    print("\n--- Resultados Finais ---")
    print(f"Total de números pares: {contagem_pares}")
    print(f"Total de números ímpares: {contagem_impares}")

# Executa a função
contar_pares_impares()