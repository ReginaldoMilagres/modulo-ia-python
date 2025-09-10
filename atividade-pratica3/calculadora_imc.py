# Calculadora de IMC

# 1 - Solicita o peso e a altura do usuário
# A função 'input()' recebe os dados como texto. 'float()' converte esse texto para um número decimal.
# O bloco 'try-except' é usado para evitar erros se o usuário digitar letras em vez de números.
try:
    peso = float(input("Digite seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite sua altura em metros (ex: 1.75): "))

    # 2 - Verifica se os valores são válidos
    # A altura e o peso não podem ser zero ou negativos. Se forem, o programa informa o erro e encerra.
    if peso <= 0 or altura <= 0:
        print("Valores inválidos. Por favor, digite um peso e altura positivos.")
    else:
        # 3 - Calcula o Índice de Massa Corporal (IMC)
        # A fórmula do IMC é: peso dividido pela altura ao quadrado.
        imc = peso / (altura ** 2)

        # 4 - Classifica o IMC de acordo com a tabela
        # Usa uma estrutura 'if-elif-else' para determinar a classificação baseada no valor do IMC.
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        # Se nenhuma das condições acima for verdadeira, o IMC é 30 ou maior.
        else:
            classificacao = "Obeso"

        # 5 - Exibe os resultados
        # Imprime o valor do IMC formatado (arredondado para duas casas decimais) e a sua classificação.
        print("\n--- Resultado do seu IMC ---")
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")

# Lida com o erro caso a entrada do usuário não possa ser convertida para um número.
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números para peso e altura.")