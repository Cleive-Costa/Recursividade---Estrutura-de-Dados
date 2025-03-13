def investimento_acoes(valor_atual=0, meses=0, valor_investido=0, dividendos_acumulados=0, marco_100k=False, marco_1m=False):
    # Dados das ações (preço e dividendos mensais em 2024)
    acoes = {
        "AÇÃO1": {"preco": [50, 52, 55, 53, 56, 58, 60, 62, 65, 67, 70, 72], "dividendo": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]},
        "AÇÃO2": {"preco": [100, 105, 110, 108, 112, 115, 118, 120, 125, 130, 135, 140], "dividendo": [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1]},
        "AÇÃO3": {"preco": [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], "dividendo": [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]},
    }

    # Verifica se todos os marcos foram atingidos
    if marco_100k and marco_1m:
        anos = meses // 12
        meses_restantes = meses % 12
        print(f"Tempo total: {anos} anos e {meses_restantes} meses")
        print(f"Valor total investido: R$ {valor_investido:.2f}")
        print(f"Valor final em reais: R$ {valor_atual:.2f}")
        print(f"Dividendos acumulados: R$ {dividendos_acumulados:.2f}")
        return

    # Verifica se atingiu o marco de R$ 100.000,00
    if not marco_100k and valor_atual >= 100000:
        print(f"Atingiu R$ 100.000,00 em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        print(f"Dividendos acumulados até agora: R$ {dividendos_acumulados:.2f}")
        marco_100k = True

    # Verifica se atingiu o marco de R$ 1.000.000,00
    if not marco_1m and valor_atual >= 1000000:
        print(f"Atingiu R$ 1.000.000,00 em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        print(f"Dividendos acumulados até agora: R$ {dividendos_acumulados:.2f}")
        marco_1m = True

    # Adiciona o investimento mensal de R$ 80,00
    valor_investido += 80
    valor_atual += 80

    # Calcula os dividendos e a valorização das ações
    for acao, dados in acoes.items():
        preco_mes = dados["preco"][meses % 12]  # Preço da ação no mês atual
        dividendo_mes = dados["dividendo"][meses % 12]  # Dividendo da ação no mês atual

        # Compra de cotas (proporcional ao investimento mensal)
        cotas_compradas = 80 / len(acoes) / preco_mes  # Divide o investimento entre as ações
        valor_atual += cotas_compradas * preco_mes  # Atualiza o valor atual com a valorização

        # Acumula os dividendos
        dividendos_acumulados += cotas_compradas * dividendo_mes

    # Chama a função recursivamente para o próximo mês
    investimento_acoes(valor_atual, meses + 1, valor_investido, dividendos_acumulados, marco_100k, marco_1m)

# Inicia a simulação
investimento_acoes()