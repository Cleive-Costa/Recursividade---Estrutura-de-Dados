def investimento_poupanca(valor_atual=0, meses=0, valor_investido=0, juros_acumulados=0):
    # Definição dos marcos
    marco_100k = 100000
    marco_1m = 1000000

    # Verifica se atingiu o marco de R$ 1.000.000,00
    if valor_atual >= marco_1m:
        anos = meses // 12
        meses_restantes = meses % 12
        print(f"Tempo para atingir R$ 1.000.000,00: {anos} anos e {meses_restantes} meses")
        print(f"Valor total investido: R$ {valor_investido:.2f}")
        print(f"Juros compostos obtidos: R$ {juros_acumulados:.2f}")
        print(f"Resultado final: R$ {valor_atual:.2f}")
        return

    # Verifica se atingiu o marco de R$ 100.000,00
    if valor_atual >= marco_100k and marco_100k != 0:
        print(f"Atingiu R$ 100.000,00 em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        print(f"Juros compostos até agora: R$ {juros_acumulados:.2f}")
        marco_100k = 0  # Para não exibir novamente

    # Aplica o rendimento de 0,05% após 30 dias (1 mês)
    if meses > 0:
        rendimento = valor_atual * 0.0005  # 0,05% de rendimento
        valor_atual += rendimento
        juros_acumulados += rendimento

    # Adiciona o investimento mensal de R$ 500,00
    valor_atual += 500
    valor_investido += 500

    # Chama a função recursivamente para o próximo mês
    investimento_poupanca(valor_atual, meses + 1, valor_investido, juros_acumulados)

# Inicia a simulação
investimento_poupanca()