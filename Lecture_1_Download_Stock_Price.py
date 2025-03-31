#Download AAPL stock data from yfinance(2020-01-01-2025-01-31)
import yfinance as yf
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2025-01-31'
df = yf.download(ticker, start_date, end_date)
print(df)

'''这段代码是用验证github commit是否成功的'''
'''卧槽居然成功了'''
