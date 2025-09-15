import string

def eh_palindromo(frase):
    """
    Verifica se uma palavra ou frase é um palíndromo,
    ignorando espaços e pontuação.
    
    Exemplos de palíndromos:
    A base do teto desaba;
    A cara rajada da jararaca;
    A torre da derrota;
    O lobo ama o bolo;
    Anotaram a data da maratona.
    

    Parâmetros:
    - frase (str): A string a ser verificada.

    Retorna:
    - bool: True se a frase for um palíndromo, False caso contrário.
    """
    # 1. Converte para minúsculas e remove espaços
    texto_limpo = frase.lower().replace(" ", "")
    
    # 2. Remove pontuação
    tabela_traducao = str.maketrans('', '', string.punctuation)
    texto_final = texto_limpo.translate(tabela_traducao)
    
    # 3. Compara o texto limpo com o seu reverso
    return texto_final == texto_final[::-1]

# --- Exemplo de uso da função ---
if __name__ == "__main__":
    
    # Solicita a frase ao usuário
    frase_digitada = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    
    # Chama a função para verificar
    if eh_palindromo(frase_digitada):
        print("Sim")
    else:
        print("Não")