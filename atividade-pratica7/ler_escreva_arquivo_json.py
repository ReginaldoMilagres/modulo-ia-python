import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
            print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro: {e}")

dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Recife"
}

nome_arquivo_json = input("Digite o nome do arquvo JSON: ").strip()
ler_json(nome_arquivo_json)
escrever_json(nome_arquivo_json, dados)
ler_json(nome_arquivo_json)