def calcular_media_turma():
    """
    Função para registrar notas de alunos e calcular a média da turma.
    """
    print("--- Calculadora de Média da Turma ---")
    
    # Lista para armazenar as notas de todos os alunos
    notas_da_turma = []
    
    # Loop principal para a entrada de notas
    while True:
        try:
            print("OBS: Digite 'média' ou 'media' para calcular a média dos alunos.")
            # Pede o nome do aluno
            nome_aluno = input("Digite o nome do aluno : ")
            
            # Condição de saída do loop
            if nome_aluno.lower() == 'média' or nome_aluno.lower() == 'media':
                break
            
            # Pede a nota do aluno
            nota_str = input(f"Digite a nota de {nome_aluno}: ")
            
            # Converte a nota para um número de ponto flutuante (float)
            nota = float(nota_str)
            
            # Adiciona a nota à lista
            notas_da_turma.append(nota)
            
            print(f"Nota de {nome_aluno} registrada com sucesso.")
        
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a nota.")
        
        print("---")
    
    # Verifica se alguma nota foi registrada antes de calcular a média
    if not notas_da_turma:
        print("Nenhuma nota foi registrada. Não é possível calcular a média.")
    else:
        # Soma todas as notas da lista
        soma_das_notas = sum(notas_da_turma)
        # Calcula a média dividindo a soma pelo número de notas
        media_da_turma = soma_das_notas / len(notas_da_turma)
        
        print("\n--- Resultados Finais ---")
        print(f"Total de alunos com notas registradas: {len(notas_da_turma)}")
        print(f"A média da turma é: {media_da_turma:.2f}")

# Executa a função
calcular_media_turma()