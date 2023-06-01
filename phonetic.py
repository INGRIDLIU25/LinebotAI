import requests
from bs4 import BeautifulSoup
def read(word):
    url = f'https://dict.revised.moe.edu.tw/search.jsp?md=1&word={word}#searchL'
    html=requests.get(url)
    bs=BeautifulSoup(html.text,'lxml')
    data = bs.find('table', id='searchL')
    try:
        row = data.find_all('tr')[2]
        chinese = row.find('cr').text
        phones=row.find_all('code')
        phone=[e.text for e in phones]
        #phone=data.find('td' , class_="ph").text
        s=" ".join(phone)
        return(chinese+s)
    except:
        return('找不到')
