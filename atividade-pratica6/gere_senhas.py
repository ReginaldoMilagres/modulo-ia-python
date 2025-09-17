import random
import string

def gerar_senha(tamanho):
    """
    Gera uma senha aleatória com letras, números e símbolos
    com um tamanho definido pelo usuário.
    
    Parâmetros:
    - tamanho (int): O tamanho da senha a ser gerada.
    
    Retorna:
    - str: A senha aleatória gerada ou uma mensagem de erro.
    """
    # Combina todos os caracteres possíveis
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Valida se o tamanho é um número positivo
    if tamanho <= 0:
        return "Erro: O tamanho da senha deve ser maior que zero."

    # Usa 'random.sample' para selecionar caracteres de forma aleatória
    # e sem repetição até atingir o tamanho desejado
    senha_lista = random.sample(caracteres, tamanho)
    
    # Junta a lista de caracteres em uma única string
    senha_final = "".join(senha_lista)
    
    return senha_final

# --- Interação com o usuário ---
try:
    # Solicita o tamanho da senha
    tamanho_desejado = int(input("Digite o tamanho da senha que você quer (ex: 12): "))
    
    # Chama a função e armazena o resultado
    senha_gerada = gerar_senha(tamanho_desejado)
    
    # Exibe a senha ou a mensagem de erro
    print(f"\nSua nova senha é: {senha_gerada}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")