
import  yfinance #import function

name=str(input('Please input company stock name:'))
company = yfinance.Ticker(name) #company stock name

#company stock data
stock_date_dy = company.history(period="1dy")
stock_date_we=company.history(period="1we")
stock_date_mo = company.history(period="1mo")

stock_data=[stock_date_dy, stock_date_we, stock_date_mo]

print(stock_data)#out stock data
