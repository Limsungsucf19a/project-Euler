import requests
import csv
from bs4 import BeautifulSoup

csvFile = open("f:down/cgv.csv", 'w+')

resp = requests.get('http://www.cgv.co.kr/movies/')
soup = BeautifulSoup(resp.text, 'html.parser')

tags = soup.select('strong class=' '.title')
title = tags[0].getText()
print(title)


writer = csv.writer(csvFile)

#for hotkey in hotkeywords:
#        writer.writerow(f'{hotkey.select_one("title").get_text()} '
#                        f'{hotkey.select_one("percent").get_text()} ')
for hotkey in hotkeywords:
        print( f'{hotkey.select_one("title").get_text()} '
               f'{hotkey.select_one("percent").get_text()} ')                        

                     




