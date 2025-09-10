# Verificador de Ano Bissexto

# 1 - Solicita o ano ao usuário e trata a entrada para ser um número inteiro.
# O bloco 'try-except' lida com entradas que não são números.
try:
    ano = int(input("Digite um ano: "))

    # 2 - Verifica se o ano é bissexto usando as regras específicas.
    # A estrutura 'if-elif-else' é usada para testar as condições em ordem.

    # Um ano é bissexto se for divisível por 400. Esta é a condição mais prioritária.
    if (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")

    # Se a condição acima for falsa, verifica se o ano é divisível por 4 e não por 100.
    # Isso cobre a maioria dos anos bissextos (ex: 2024, 2028).
    elif (ano % 4 == 0) and (ano % 100 != 0):
        print(f"O ano {ano} é bissexto.")

    # Se nenhuma das condições anteriores for verdadeira, o ano não é bissexto.
    # Isso inclui anos como 1900, que são divisíveis por 100 mas não por 400.
    else:
        print(f"O ano {ano} não é bissexto.")

# 3 - Lida com o erro de entrada inválida
except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido.")