import requests
import csv
from bs4 import BeautifulSoup

csvFile = open("f:down/cgv.csv", 'w+')

resp = requests.get('http://www.cgv.co.kr/movies/')
soup = BeautifulSoup(resp.text, 'html.parser')

ranks = soup.find_all(class_ = "rank")
titles = soup.find_all(class_ = "title")
grades = soup.find_all(class_ = "ico-grade") 
infos = soup.find_all(class_ = "txt-info")


for i in range(0,7):
    print(ranks[i].get_text(), titles[i].get_text(), 
          grades[i].get_text(), infos[i].get_text())

writer = csv.writer(csvFile)

for i in range(0,7):
   writer.writerow([ranks[i].get_text(), titles[i].get_text(),
                    grades[i].get_text(), infos[i].get_text()])

csvFile.close()
                     




