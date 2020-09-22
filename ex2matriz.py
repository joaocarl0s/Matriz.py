matriz = []                 #Matriz realizará um append de uma linha inteira. [[0,0,0]]. Até cumprir o range(5).

for i in range(5):          #Matriz de 5 linhas.
    linha = []              #Linha será auxiliar e sempre começará vazia.
    for j in range(3):      #3 colunas.                    j = 1   >     j = 2     >     j = 3
        linha.append(0)                               #linha = [0] > linha = [0,0] > linha = [0,0,0]
    matriz.append(linha)

print("\n")
for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
    print()