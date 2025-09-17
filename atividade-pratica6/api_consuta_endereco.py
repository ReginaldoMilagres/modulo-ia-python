import requests

def consultar_cep():
    """
    Consulta a API do ViaCEP para buscar dados de um endereço
    a partir de um CEP.
    """
    print("--- Consulta de Endereço por CEP ---")
    
    # Pede o CEP ao usuário
    cep = input("Digite o CEP (apenas números): ")
    
    # Remove espaços ou hífens para garantir o formato correto
    cep_limpo = cep.replace("-", "").strip()
    
    # Valida o formato do CEP (deve ter 8 dígitos)
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print("\nFalha: O CEP digitado é inválido. Por favor, digite 8 dígitos.")
        return
    
    # Constrói a URL da API com o CEP fornecido
    url_api = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        # Faz a requisição à API
        resposta = requests.get(url_api, timeout=10)
        
        # Lança um erro se a requisição não for bem-sucedida (ex: 404, 500)
        resposta.raise_for_status()
        
        # Converte a resposta JSON da API para um dicionário Python
        dados = resposta.json()
        
        # A API retorna um campo 'erro' se o CEP não for encontrado
        if 'erro' in dados and dados['erro']:
            print("\nFalha: O CEP digitado não foi encontrado.")
        else:
            # Exibe os dados do endereço
            print("\n--- Endereço Encontrado ---")
            print(f"Logradouro: {dados.get('logradouro', 'Não disponível')}")
            print(f"Bairro: {dados.get('bairro', 'Não disponível')}")
            print(f"Cidade: {dados.get('localidade', 'Não disponível')}")
            print(f"Estado: {dados.get('uf', 'Não disponível')}")
            
    except requests.exceptions.RequestException:
        # Captura erros de conexão, como falta de internet ou URL incorreta
        print("\nFalha na conexão: Não foi possível acessar a API. Verifique sua conexão com a internet.")

# Executa a função
consultar_cep()