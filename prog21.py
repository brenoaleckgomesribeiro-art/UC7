soma = 0
valor = 1

while valor:
    valor = int(input("Digite o seu valor: "))
    
    if valor == 0:
        break
    
    soma = soma + valor
    print(f"Soma atual: {soma}")

print(f"Soma final: {soma}")

