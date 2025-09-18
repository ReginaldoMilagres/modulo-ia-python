import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

nome_arquivo_csv = input("Digite o nome do arquivo CSV: ").strip()
ler_csv(nome_arquivo_csv)