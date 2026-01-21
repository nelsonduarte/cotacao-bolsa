import pandas as pd
import yfinance as yf

opcao = "" # variavel de controle

while True:
    print("\n-------- Cotação de Ações --------\n")
    
    nome_acao = input("Insira o nome da ação em bolsa que deseja obter informações: ")
    data_inicio = input("Insira uma data de inicio: ")
    data_fim = input("Insira uma data de fim: ")

    # obter os dados de cotação em bolsa 
    df = yf.download(nome_acao, start=data_inicio, end=data_fim)
    print(df)

    opcao = input("\nDeseja continuar? (s/n) ").lower()

    if opcao == 'n':
        break

