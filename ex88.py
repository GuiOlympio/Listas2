from random import randint

# Inicializa listas para armazenar os números sorteados e os jogos
lista = []
jogos = []

# Pergunta ao usuário quantos jogos ele quer gerar
quant = int(input("Quantos jogos? "))

# Loop para gerar os jogos
tot = 1
while tot <= quant:
    cont = 0
    # Loop para gerar 6 números distintos por jogo
    while cont < 6:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1  # Incrementa o contador para parar após 6 números
    lista.sort()  # Ordena os números gerados
    jogos.append(lista[:])  # Adiciona o jogo à lista de jogos
    lista.clear()  # Limpa a lista para o próximo jogo
    tot += 1

# Exibe os jogos gerados
for i, l in enumerate(jogos):
    print(f"Jogo {i + 1}: {l}")
