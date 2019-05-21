import requests
import csv
from bs4 import BeautifulSoup

csvFile = open("f:down/auction.csv", 'w+')

resp = requests.get('http://www.cgv.co.kr/movies/')
soup = BeautifulSoup(resp.text, 'html.parser')

hotkeywords = soup.select('.title')

writer = csv.writer(csvFile)

for hotkey in hotkeywords:
        writer.writerow(f'{hotkey.select_one(".title").get_text()} '
                        f'{hotkey.select_one(".title").get_text()} ')




