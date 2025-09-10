# Conversor de Temperatura
print("OBS: C = CELSIUS - F = FAHRENHEIT! - K = KELVIN")

# 1 - Solicita a temperatura e as unidades de origem e destino
# O bloco 'try-except' é usado para tratar erros de entrada, como o usuário digitar letras no lugar de números.
try:
    temperatura = float(input("Digite a temperatura: "))
    # Converte as unidades de entrada para letras maiúsculas para facilitar a comparação.
    unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
    unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()

    # 2 - Verifica a unidade de origem e aplica a conversão correta
    # A estrutura 'if-elif-else' permite escolher a fórmula certa com base nas unidades informadas.

    if unidade_origem == 'C':
        # Converte de Celsius para outras unidades
        if unidade_destino == 'F':
            resultado = (temperatura * 9/5) + 32
        elif unidade_destino == 'K':
            resultado = temperatura + 273.15
        elif unidade_destino == 'C':
            # Caso a origem e o destino sejam os mesmos
            resultado = temperatura
        else:
            # Lida com uma unidade de destino inválida
            print("Unidade de destino inválida.")
            resultado = None  # Define o resultado como nulo para evitar a impressão
    
    elif unidade_origem == 'F':
        # Converte de Fahrenheit para outras unidades
        if unidade_destino == 'C':
            resultado = (temperatura - 32) * 5/9
        elif unidade_destino == 'K':
            resultado = (temperatura - 32) * 5/9 + 273.15
        elif unidade_destino == 'F':
            resultado = temperatura
        else:
            print("Unidade de destino inválida.")
            resultado = None
            
    elif unidade_origem == 'K':
        # Converte de Kelvin para outras unidades
        if unidade_destino == 'C':
            resultado = temperatura - 273.15
        elif unidade_destino == 'F':
            resultado = (temperatura - 273.15) * 9/5 + 32
        elif unidade_destino == 'K':
            resultado = temperatura
        else:
            print("Unidade de destino inválida.")
            resultado = None

    else:
        # Lida com uma unidade de origem inválida
        print("Unidade de origem inválida.")
        resultado = None

    # 3 - Exibe o resultado da conversão se for válido
    # A condição 'if resultado is not None' garante que o programa só imprima o resultado se
    # a conversão tiver sido bem-sucedida, evitando erros.
    if resultado is not None:
        print(f"\n{temperatura:.2f} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}.")

# Lida com o erro caso o usuário digite algo que não seja um número.
except ValueError:
    print("Entrada inválida. Por favor, digite um valor numérico para a temperatura.")