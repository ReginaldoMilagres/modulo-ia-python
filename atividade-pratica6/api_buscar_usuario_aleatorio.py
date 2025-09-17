import requests

def buscar_usuario_aleatorio():
    """
    Acessa a API de usuário fictício e exibe seus dados,
    tratando possíveis erros de conexão.
    """
    # URL da API que fornece um usuário fictício aleatório
    url = "https://randomuser.me/api/"
    
    try:
        # Tenta fazer a requisição HTTP GET para a API
        # O 'timeout' impede que o programa fique esperando para sempre
        resposta = requests.get(url, timeout=5)
        
        # Verifica se a resposta tem um status de erro (4xx ou 5xx)
        # Se sim, lança uma exceção que o 'except' irá capturar
        resposta.raise_for_status()
        
        # Analisa a resposta JSON da API e a converte em um dicionário Python
        dados = resposta.json()
        
        # Extrai os dados do primeiro (e único) usuário no resultado
        usuario = dados['results'][0]
        
        # Formata as informações para exibição
        nome_completo = f"{usuario['name']['title']}. {usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Exibe os dados do usuário na tela
        print("--- Usuário Fictício Aleatório ---")
        print(f"Nome: {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    
    except requests.exceptions.RequestException:
        # Captura qualquer erro de conexão (falta de internet, URL inválida, etc.)
        print("--- Falha na Conexão ---")
        print("Erro: Não foi possível acessar a API. Por favor, verifique sua conexão com a internet ou tente novamente.")

# Executa a função para iniciar o programa
buscar_usuario_aleatorio()