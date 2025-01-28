# Criação de uma matriz 3x3 preenchida inicialmente com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Loop para percorrer as linhas da matriz
for l in range(3):
    # Loop para percorrer as colunas da matriz
    for c in range(3):
        # Solicita um número ao usuário e armazena na posição correspondente da matriz
        matriz[l][c] = int(input('Digite um número: '))

# Exibição da matriz formatada
for l in range(3):
    for c in range(3):
        # Exibe os valores da matriz na mesma linha
        print(matriz[l][c], end=' ')
    # Pula para a próxima linha após exibir uma linha completa da matriz
    print()
