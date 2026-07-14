soma = 0
codigo = -1

print("--- Caixa de Supermercado Simples ---")
print("Produtos:")
print("001 - Arroz (R$ 4,00)")
print("002 - Feijão (R$ 7,00)")
print("003 - Macarrão (R$ 5,00)")
print("Digite 0 para finalizar a conta")

while codigo != 0:
    codigo = int(input("Digite o código: "))

    if codigo == 0:
        break
    elif codigo == 001:
        soma = soma + 4
        print(f"Total da compra: R$ {soma}")
    elif codigo == 002:
        soma = soma + 7
        print(f"Total da compra: R$ {soma}")
    elif codigo == 003:
        soma = soma + 5
        print(f"Total da compra: R$ {soma}")
    else:
        print("Código inválido!")

print(f"Valor final da compra: R$ {soma}")