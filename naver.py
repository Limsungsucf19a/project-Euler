import requests
from bs4 import BeautifulSoup

# 소스코드에서 클래스 찾기 
# class에
#  

resp = requests.get('https://www.naver.com/')
soup = BeautifulSoup(resp.text, 'html.parser')

hotkeywords = soup.select('.ah_list .ah_item')
hotnews = soup.select('.ca_item')

for hotkey in hotkeywords:
    print(f'{hotkey.select_one(".ah_r").get_text()}위 '
          f'{hotkey.select_one(".ah_k").get_text()} ')

for news in hotnews:
    print(f'{news.select_one(".ca_a").get_text()} ')



