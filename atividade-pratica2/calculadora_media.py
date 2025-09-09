# 3. Calculadora de Média Escolar

# Solicita as notas do aluno ao usuário
# A função input() lê o valor digitado como texto, e float() o converte para número decimal.
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

# Calcula a soma das notas
# Soma as três notas para o cálculo da média.
soma_notas = nota1 + nota2 + nota3

# Calcula a média aritmética
# A média é o resultado da divisão da soma das notas pela quantidade de notas.
media = soma_notas / 3

# Exibe as notas inseridas e o resultado da média final
# Utiliza f-strings para uma apresentação clara e formatada dos valores,
# arredondando a média para duas casas decimais com .2f para melhor visualização.
print("\n--- Notas e Média ---")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("---------------------")
print(f"Média final: {media:.2f}")