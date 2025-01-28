# Inicialização de listas: `temp` para armazenar dados temporários e `princ` para os dados principais
temp = []
princ = []
# Variáveis para armazenar o maior e menor peso
maior = menor = 0

# Início de um loop infinito para cadastrar pessoas
while True:
    # Adiciona o nome na lista temporária
    temp.append(str(input("Nome: ")))
    # Adiciona o peso na lista temporária
    temp.append(float(input("Peso: ")))

    # Na primeira iteração, define o primeiro peso como maior e menor
    if len(princ) == 0:        
        maior = menor = temp[1]
    else:
        # Atualiza o maior peso, se o peso atual for maior
        if temp[1] > maior:
            maior = temp[1]
        # Atualiza o menor peso, se o peso atual for menor
        elif temp[1] < menor:
            menor = temp[1]

    # Faz uma cópia dos dados temporários e adiciona na lista principal
    princ.append(temp[:])
    # Limpa a lista temporária para a próxima entrada
    temp.clear()

    # Loop para validar a resposta do usuário (se deseja continuar ou não)
    resp = ' '
    while resp not in "SN":
        resp = input("Continuar? [S/N] ").strip().upper()[0]
    # Se o usuário escolher "N", o loop principal será encerrado
    if resp == 'N':
        break

# Exibe o número total de pessoas cadastradas
print(f"\nTotal de pessoas cadastradas: {len(princ)}")

# Exibe o maior peso e os nomes associados a ele
print(f"O maior peso foi {maior}kg. Peso de: ", end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()

# Exibe o menor peso e os nomes associados a ele
print(f"O menor peso foi {menor}kg. Peso de: ", end="")
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()
