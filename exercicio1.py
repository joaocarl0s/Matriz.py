# 1)Crie um programa em Python que preencha uma matriz
# (lista de lista) 7x2 com números inteiros informados pelo usuário.
# Mostre a quantidade de elementos entre 10 e 20 (inclusive).

matriz = []
count = 0

for l in range(2):
    linha = []
    for c in range(2):
        num = int(input("Digite um número: "))
        linha.append(num)
        if num >= 10 and num <= 20:
            count += 1
    matriz.append(linha)

print("\n")
for lista in matriz:
    for linha in lista:
        print(linha, end=' ')
    print()

print("\n")
if count == 1:
    print("Houve",count,"número entre 10 e 20.")
elif count > 1:
    print("Houve", count, "números entre 10 e 20.")
else:
    print("Não houve números entre 10 e 20.")

