# 2) Faça um programa em Python que realiza a soma de duas matrizes 2x2.
# Importante: O usuário entrará com os valores (números inteiros) que preencherá as duas matrizes (a e b).
# Mostrar na tela a terceira matriz (c) com a soma de a + b.

matriz_a = []
matriz_b = []
matriz_c = []

for l in range(2):
    linha_a = []
    linha_b = []
    linha_c = []
    for c in range(2):
        num = int(input("Digite um número: "))
        num2= int(input("Digite um número: "))
        linha_a.append(num)
        linha_b.append(num2)
        soma = num + num2
        linha_c.append(soma)
    matriz_a.append(linha_a)
    matriz_b.append(linha_b)
    matriz_c.append(linha_c)



print("\n")
for lista in matriz_a:
    for linha in lista:
        print(linha, end=' ')
    print()

print(" +")

for lista in matriz_b:
    for linha in lista:
        print(linha, end=' ')
    print()

print("=")


for lista in matriz_c:
    for linha in lista:
        print(linha, end=' ')
    print()

