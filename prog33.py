'''
def nota_final(n1,n2,n3,n4):
    nota = n1 + n2 + n3 + n4 
    print(f"A média do aluno é {soma} por tanto, o aluno está {media}")

soma = 0

n1 = float(input("Digite sua nota: "))
n2 = float(input("Digite sua nota: "))
n3 = float(input("Digite sua nota: "))
n4 = float(input("Digite sua nota: "))
soma = n1 + n2 + n3 + n4
media = soma / 4 

if media >= 7:
    print("aprovado")

elif media >= 5:
    print("em recuperação")
else:
    print("reprovado")

nota_final(n1,n2,n3,n4)

'''
def nota_final(n1, n2, n3, n4):
    soma = n1 + n2 + n3 + n4
    media = soma / 4

    if media >= 7:
        situacao = "aprovado"
    elif media >= 5:
        situacao = "em recuperação"
    else:
        situacao = "reprovado"

    print(f"A média do aluno é {media}. Portanto, o aluno está {situacao}.")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

nota_final(n1, n2, n3, n4)
