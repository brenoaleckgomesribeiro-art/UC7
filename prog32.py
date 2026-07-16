def ano(n):
    resultado = 2026 - n
    return resultado

nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano(nascimento)

if idade >= 65:
    print("Você é idoso")
elif idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")