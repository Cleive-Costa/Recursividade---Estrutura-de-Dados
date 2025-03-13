def investimento_bitcoin(valor_atual=0, meses=0, valor_investido=0, bitcoins=0, marco_100k=False, marco_1m=False, marco_1btc=False):
    # Cotação mensal do Bitcoin em 2024 (valores fictícios, ajuste conforme necessário)
    cotacao_bitcoin_2024 = [
        200000, 205000, 210000, 215000, 220000, 225000,  # Janeiro a Junho
        230000, 235000, 240000, 245000, 250000, 255000   # Julho a Dezembro
    ]

    # Verifica se todos os marcos foram atingidos
    if marco_100k and marco_1m and marco_1btc:
        anos = meses // 12
        meses_restantes = meses % 12
        print(f"Tempo total: {anos} anos e {meses_restantes} meses")
        print(f"Valor total investido: R$ {valor_investido:.2f}")
        print(f"Valor final em reais: R$ {valor_atual:.2f}")
        print(f"Quantidade de Bitcoins acumulados: {bitcoins:.8f} BTC")
        return

    # Verifica se atingiu o marco de R$ 100.000,00
    if not marco_100k and valor_atual >= 100000:
        print(f"Atingiu R$ 100.000,00 em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        marco_100k = True

    # Verifica se atingiu o marco de R$ 1.000.000,00
    if not marco_1m and valor_atual >= 1000000:
        print(f"Atingiu R$ 1.000.000,00 em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        marco_1m = True

    # Verifica se atingiu o marco de 1 Bitcoin
    if not marco_1btc and bitcoins >= 1:
        print(f"Atingiu 1 Bitcoin em {meses} meses.")
        print(f"Valor investido até agora: R$ {valor_investido:.2f}")
        marco_1btc = True

    # Adiciona o investimento mensal de R$ 250,00
    valor_atual += 250
    valor_investido += 250

    # Calcula a cotação do Bitcoin no mês atual (usando o índice do mês)
    cotacao_mes = cotacao_bitcoin_2024[meses % 12]  # Repete a lista após 12 meses
    bitcoins += 250 / cotacao_mes  # Converte R$ 250 em Bitcoin

    # Chama a função recursivamente para o próximo mês
    investimento_bitcoin(valor_atual, meses + 1, valor_investido, bitcoins, marco_100k, marco_1m, marco_1btc)

# Inicia a simulação
investimento_bitcoin()