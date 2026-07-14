print("--- Restaurante ---")
print("Digite 0 para finalizar a conta")

total = 0
valor = -1

while valor != 0:
    valor = int(input("Digite o valor do item: R$ "))

    if valor == 0:
        break

    total = total + valor
    print(f"Total parcial: R$ {total}")

gorjeta = total * 0.1
valor_total = total + gorjeta

print(f"Gorjeta (10%): R$ {gorjeta}")
int(input("Deseja adcionar gorjeta? 0 pra sim e 1 pra não: "))

if valor_total == 0:
    print("Total com gorjeta:{valor_final}")

elif valor_total == 1:
    print("Total sem gorjeta:{total}")