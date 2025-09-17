import requests
from datetime import datetime

def consultar_cotacao_brl():
    """
    Consulta o valor do Real (BRL) em relação a outra moeda usando
    a AwesomeAPI, exibindo o valor atual, máximo, mínimo e a data
    da última atualização.
    """
    print("--- Consulta de Cotação do Real (BRL) ---")
    
    # Pede ao usuário a moeda para comparação. USD é o padrão.
    print("Moedas disponíveis: USD = DOLAR, EUR = EURO, JPY = IENE JAPONES, ")
    moeda_alvo = input("Digite a moeda para comparação (ex: USD, EUR, JPY). Pressione Enter para USD: ").upper()
    if not moeda_alvo:
        moeda_alvo = "USD"
        
    par_moedas = f"{moeda_alvo}-BRL"
    url_api = f"https://economia.awesomeapi.com.br/json/last/{par_moedas}"
    
    try:
        # Tenta fazer a requisição HTTP para a API
        resposta = requests.get(url_api, timeout=10)
        
        # Lança uma exceção para códigos de status de erro (4xx, 5xx)
        resposta.raise_for_status()
        
        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()
        
        # A API retorna um dicionário vazio se o par de moedas não existir
        if not dados:
            print(f"\nErro: O par de moedas '{par_moedas}' não foi encontrado.")
            return
            
        # A chave do dicionário é dinâmica (ex: 'USDBRL')
        cotacao_data = dados.get(par_moedas.replace('-', ''))
        
        if not cotacao_data:
            print(f"\nErro: Dados para o par '{par_moedas}' não encontrados na resposta da API.")
            return
        
        # Extrai e converte os dados relevantes
        valor_atual = float(cotacao_data['bid'])
        valor_maxima = float(cotacao_data['high'])
        valor_minima = float(cotacao_data['low'])
        timestamp_atualizacao = int(cotacao_data['timestamp'])
        
        # Converte o timestamp Unix para um formato de data/hora legível
        data_atualizacao = datetime.fromtimestamp(timestamp_atualizacao).strftime('%d/%m/%Y %H:%M:%S')
        
        # Exibe os resultados
        print(f"\n--- Cotação {par_moedas} ---")
        print(f"Valor Atual: R$ {valor_atual:.2f}")
        print(f"Máxima (24h): R$ {valor_maxima:.2f}")
        print(f"Mínima (24h): R$ {valor_minima:.2f}")
        print(f"Última atualização: {data_atualizacao}")
        
    except requests.exceptions.RequestException:
        # Captura erros de conexão, como falta de internet
        print("\nErro de conexão: Não foi possível acessar a API. Verifique sua conexão com a internet.")
    except (ValueError, KeyError, IndexError):
        # Captura erros se a estrutura da resposta da API mudar
        print("\nErro: Houve um problema ao processar os dados da API. O formato pode ter sido alterado.")

# Executa a função
consultar_cotacao_brl()