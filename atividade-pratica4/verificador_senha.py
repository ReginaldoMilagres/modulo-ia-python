def verificar_senha():
    """
    Verifica se a senha digitada pelo usuário atende aos critérios de segurança.
    Critérios:
    - Pelo menos 8 caracteres
    - Pelo menos um número
    """
    print("--- Verificador de Segurança de Senha ---")
    
    # Solicita a senha do usuário
    senha = input("Crie uma senha: ")
    
    # Variáveis de controle para os critérios
    tem_oito_caracteres = False
    tem_um_numero = False
    
    # --- Passo 1: Verifica o comprimento da senha ---
    if len(senha) >= 8:
        tem_oito_caracteres = True
    
    # --- Passo 2: Verifica se há pelo menos um número ---
    # Percorre cada caractere da senha
    for caractere in senha:
        # Verifica se o caractere é um dígito (número)
        if caractere.isdigit():
            tem_um_numero = True
            # Se encontrar um número, não precisa continuar o loop
            break
            
    # --- Passo 3: Apresenta o resultado para o usuário ---
    print("\nAnálise da senha:")
    
    # Verifica e informa se cada critério foi atendido
    if tem_oito_caracteres:
        print("✅ A senha tem 8 ou mais caracteres.")
    else:
        print("❌ A senha deve ter no mínimo 8 caracteres.")
        
    if tem_um_numero:
        print("✅ A senha contém pelo menos um número.")
    else:
        print("❌ A senha deve conter pelo menos um número.")
        
    # Mensagem final com o resultado geral
    if tem_oito_caracteres and tem_um_numero:
        print("\n😄 Sua senha atende a todos os critérios de segurança!")
    else:
        print("\n⚠️ Por favor, melhore sua senha para atender aos critérios.")

# Executa a função
verificar_senha()