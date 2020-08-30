import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup
def StockPrice(stock_code):
    url = ("https://finance.yahoo.com/quote/")+ stock_code +('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
    response= requests.get(url)
    soup =BeautifulSoup(response.text,'lxml')
    price=soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    if price==[]:
        price='99999'
    return price
HSI = ['0001','0002','0003','0005']
for step in range(1,101):
    price= []
    col= []
    time_stamp= datetime.datetime.now()
    time_stamp= time_stamp.strftime("%Y-%m-%d %H:%M:%S" )
    for stock_code in HSI:
        price.append(StockPrice(stock_code))

    price.append(StockPrice('0001'))
    col= [time_stamp]
    col.extend(price)
    df =pd.DataFrame(col)
    df= df.T
    df.to_csv("real time stock data.csv", mode='a',header=False)
    print(col)
