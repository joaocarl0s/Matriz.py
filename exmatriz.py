matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)

#Maneira 1 de mostrar na tela:

for l in range(len(matriz)):          #l = 0 representa a linha. Quando o laço é reiniciado o l = 1, e ele pula uma linha, e assim por diante.
    print("\n")
    for c in range(len(matriz[l])):   #Ele fara de acordo com o número de elementos presentes nas listas dentro das listas.
        print(matriz[l][c], end=' ' ) #c = 0 representa a coluna. Toda vez que este for é iniciado, o range volta a valer 0.
                                      #Para cada linha faço todas as colunas pra depois mudar de linha.
                                      #Para cada for externo eu termino o for interno para depois mudar o for externo.
                                      #end serve para imprimir na mesma linha. Sem ele será impresso um embaixo do outro.

#Maneira 2 de mostra na tela:

for lista in matriz:                #lista = indíces da lista que esta dentro da lista matriz.
    for elemento in lista:
        print(elemento, end=' ')
    print()