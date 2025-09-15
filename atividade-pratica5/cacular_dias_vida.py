from datetime import date

def calcular_dias_vivos():
    """
    Calcula quantos dias um indivíduo está vivo com base na data de nascimento
    e na data atual.
    """
    print("--- Calculadora de Dias de Vida ---")
    
    # Coleta a data de nascimento do usuário
    try:
        dia = int(input("Digite o dia de nascimento (ex: 29): "))
        mes = int(input("Digite o mês de nascimento (ex: 8): "))
        ano = int(input("Digite o ano de nascimento (ex: 1990): "))
        
        data_nascimento = date(ano, mes, dia)
        data_atual = date.today()
        
        # 1. Valida se a data de nascimento é válida e não é no futuro
        if data_nascimento > data_atual:
            print("Erro: A data de nascimento não pode ser no futuro.")
            return
        
        # 2. Calcula a diferença entre as datas
        diferenca = data_atual - data_nascimento
        
        # 3. Exibe o resultado
        print("\n--- Resultado ---")
        print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
        print(f"Data atual: {data_atual.strftime('%d/%m/%Y')}")
        print(f"\nVocê está vivo há {diferenca.days} dias.")
        
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros para dia, mês e ano.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Executa a função
calcular_dias_vivos()