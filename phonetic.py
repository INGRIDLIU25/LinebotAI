import requests
from bs4 import BeautifulSoup
def read (word):
    url = f'https://tw.dictionary.search.yahoo.com/search;_ylt=Awrt4EKUS4hk85ovqBF9rolQ;_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyA3NmcARmcjIDc2EtZ3AtdHcuZGljdGlvbmFyeS5zZWFyY2gEZ3ByaWQDYlluTlFGeDRRNml1UTllTWVDSEZXQQRuX3JzbHQDMARuX3N1Z2cDNQRvcmlnaW4DdHcuZGljdGlvbmFyeS5zZWFyY2gueWFob28uY29tBHBvcwMxBHBxc3RyA2VuaGEEcHFzdHJsAzQEcXN0cmwDNwRxdWVyeQNlbmhhbmNlBHRfc3RtcAMxNjg2NjUzODQ5BHVzZV9jYXNlAw--?p={word}&fr2=sa-gp-tw.dictionary.search&fr=sfp'
    html = requests.get( url )
    bs = BeautifulSoup(html.text,'lxml')
    data=bs.find_all('h4')[0:2]
    data1=data[0].text
    if len(data) ==0 :
        return('查無此單字')
    elif len(data) ==1:
        return(word + '=>' + data1)
    elif len(data) >1 :
        return(word + data[1].text)
        return(word + '=>'+ data1)
    else:
        return('查無此單字')
