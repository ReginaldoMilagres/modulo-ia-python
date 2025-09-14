def calculadora():
    """
    Função de uma calculadora simples que realiza as quatro operações básicas.
    """
    print("--- Calculadora Simples ---")
    print("Operações disponíveis: +, -, *, /")
    
    while True:
        # Pede para o usuário inserir a operação desejada
        operacao = input("Digite a operação (+, -, *, /) ou 's' para sair: ")

        # Verifica se o usuário quer sair do programa
        if operacao.lower() == 's':
            print("Encerrando a calculadora. Até mais!")
            break

        # Verifica se a operação inserida é válida
        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida. Por favor, tente novamente.")
            continue
        
        try:
            # Pede para o usuário inserir os dois números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            # Realiza a operação com base na escolha do usuário
            if operacao == '+':
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            elif operacao == '-':
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            elif operacao == '*':
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            elif operacao == '/':
                # Adiciona um tratamento de erro para divisão por zero
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
        
        print("---")

# Chama a função para iniciar a calculadora
calculadora()