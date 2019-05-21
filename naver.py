import requests
from bs4 import BeautifulSoup

import csv
csvFile = open("../auction.csv", 'w+')
try :
    writer = csv.writer(csvFile)
    writer.writerow(('number','number2','number3'))
    for i in range(20):
        writer.writerow((i,i+2,i*2))
finally:

resp = requests.get('http://www.auction.co.kr')
soup = BeautifulSoup(resp.text, 'html.parser')

hotkeywords = soup.select('.ah_list .ah_item')
hotnews = soup.select('.ca_item')

for hotkey in hotkeywords:
    print(f'{hotkey.select_one(".ah_r").get_text()} '
          f'{hotkey.select_one(".ah_k").get_text()} ')




