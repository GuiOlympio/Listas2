# Inicializa a lista 'num' com duas sublistas vazias, uma para números pares e outra para números ímpares
num = [[],[]]

# Laço de repetição para pedir ao usuário 8 números
for c in range(8):
    # Solicita um número ao usuário
    n = int(input('Digite um número: '))
    
    # Se o número for par, adiciona na sublista num[0] (pares)
    if n % 2 == 0:
        num[0].append(n)
    # Se o número for ímpar, adiciona na sublista num[1] (ímpares)
    else:
        num[1].append(n)

    # Ordena as sublistas em ordem crescente a cada novo número inserido
    num[0].sort()
    num[1].sort()

# Exibe as listas após a coleta e ordenação dos números
print(num)
