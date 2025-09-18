import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
        print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro: {e}")

dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Pedro', 34, 'São Paulo'],
    ['Maria', 30, 'Salvador']
]

nome_arquivo_csv = input("Digite o nome do arquivo CSV: ").strip()
escrever_csv(nome_arquivo_csv, dados)