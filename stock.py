import requests
from bs4 import BeautifulSoup
def StockPrice():
    url = input()
    response= requests.get(url)
    soup =BeautifulSoup(response.text,'lxml')
    price=soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    print(price)
while True:
    StockPrice()
