# Inicializa uma lista vazia para armazenar os dados dos alunos
boletim = []

# Loop principal para cadastrar os alunos
while True:
    # Solicita o nome do aluno
    nome = str(input('Nome: '))
    
    # Solicita as duas notas do aluno
    notaP = float(input('Nota 1: '))
    notaS = float(input('Nota 2: '))
    
    # Calcula a média das notas
    media = (notaP + notaS) / 2
    
    # Adiciona os dados do aluno na lista boletim:
    # Estrutura: [Nome, [Nota1, Nota2], Média]
    boletim.append([nome, [notaP, notaS], media])
    
    # Controle de repetição - pergunta se deseja continuar
    r = ' '
    while r not in 'SN':  # Garante que apenas 'S' ou 'N' sejam aceitos
        r = str(input('Continuar [S/N]?: ')).strip().upper()[0]
    
    # Se o usuário digitar 'N', o loop encerra
    if r == 'N':
        break

# Exibe um cabeçalho formatado
print('=-' * 30)
print(f"{'N°':<5}{'Nome':<12}{'Média':>8}")  # Cabeçalho alinhado
print('=-' * 30)

# Percorre a lista e exibe os alunos cadastrados com suas médias
for i, b in enumerate(boletim):
    print(f'{i:<5}{b[0]:<12}{b[2]:>8}')  # Exibe o número, nome e média do aluno

# Loop para exibir as notas de um aluno específico
while True:
    # Solicita um número para selecionar um aluno
    selec = int(input("Selecione o número do aluno: "))
    
    # Verifica se o número é válido dentro da lista
    if selec <= len(boletim) - 1:
        print(f'Notas de {boletim[selec][0]} são {boletim[selec][1]}')
    
    # Controle de repetição - pergunta se deseja continuar
    r = ' '
    while r not in 'SN':  # Garante que apenas 'S' ou 'N' sejam aceitos
        r = str(input('Continuar [S/N]?: ')).strip().upper()[0]
    
    # Se o usuário digitar 'N', o loop encerra
    if r == 'N':
        break
