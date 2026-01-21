import pandas as pd
import yfinance as yf

# obter os dados de cotação em bolsa 
df = yf.download('AAPL', start='2025-12-01', end='2025-12-31')
print(df)
