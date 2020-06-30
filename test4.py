price = ''

import requests
import csv

from bs4 import BeautifulSoup

url = 'http://kakaku.com/kuruma/used/spec/Maker=1/Model=31773'
html = requests.get(url)

soup = BeautifulSoup(html.text,"html.parser")
span = soup.find_all("span",{"class":"price"})

for i in span:
    print(i.string)
    b =(i.string)

a_list = []
for j in b:
    a_list.append(j)

f = open('some.csv', 'w')
writer = csv.writer(f)
writer.writerow(a_list)