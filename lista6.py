curso = ["Programação com Python","Programação com Java"]
print("Bem vindo a senac")
print(f" Temos {curso}")
n = input("\nDigite o curso que deseja adcionar: ")
curso.append(n)
curso.sort()
for x in curso:
    print(f"Lista de curso Atualizada Curso: {x}")
p = input("\nAgora digite um curso que deseja retirar: ")
curso.remove(p)
curso.sort()
print(f"\nLista de curso Atualizada  com Remoção-> {curso}")

