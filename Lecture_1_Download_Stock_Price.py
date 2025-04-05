#Download AAPL stock data from yfinance(2020-01-01-2025-01-31)
import yfinance as yf
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2025-01-31'
df = yf.download(ticker, start_date, end_date)
print(df)

'''这段代码是用验证github commit是否成功的'''
'''卧槽居然成功了'''

'''
重装电脑后的push测试
'''

lst = [1,2,3,4,5]
print(lst)
lst.append(6)
print(lst)

'''成功了嘿嘿'''