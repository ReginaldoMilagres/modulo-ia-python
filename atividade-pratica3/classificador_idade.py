# 1. Classificador de Idade

# 1 - Solicita a idade do usuário e trata possíveis erros
# O bloco 'try-except' é usado para lidar com entradas inválidas, como letras ou números negativos.
try:
    # A função 'input()' lê o que o usuário digita.
    # 'int()' tenta converter o texto digitado em um número inteiro.
    idade = int(input("Digite sua idade: "))

    # 2 - Verifica se a idade é um número não-negativo.
    if idade < 0:
        print("Insira uma idade válida.")
    # 3 - Usa uma estrutura de decisão 'if-elif-else' para classificar a idade.
    # A ordem das verificações é importante para que a lógica funcione corretamente.
    elif idade <= 12:
        print("Você é uma Criança.")
    elif idade <= 17:
        print("Você é um Adolescente.")
    elif idade <= 59:
        print("Você é um Adulto.")
    elif idade >= 60 and idade <= 120:
        print("Você é um Idoso.")    
    # Se nenhuma das condições anteriores for verdadeira, a idade deve ser idade de idoso até 120, maior número invalido.
    else:
        print("Insira uma idade 0 á 120 anos.")

# 4 - Lida com o erro caso o usuário digite algo que não seja um número inteiro.
# Se a conversão 'int()' falhar (por exemplo, se o usuário digitar 'abc'), este bloco de código é executado.
except ValueError:
    print("Insira uma idade válida.")