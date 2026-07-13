senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativas = input(f"Digite sua senha(Tentativa{tentativas + 1}/{max_tentativas}): ")
    
    if tentativas == senha_correta:
        print("Acesso concedido! Bem-vindo.")
        break
    else:
        print("Senha incorreta.")
        tentativas += 1
else:
    print("Você excede o número maximo e tentativas. Acesso Bloqueado.")