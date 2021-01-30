import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://kr.investing.com/currencies/usd-krw-historical-data'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

f = open('환율', 'w', encoding='utf-8-sig', newline='') # newline 자동 줄바꿈 ''로 없앰
writer = csv.writer(f)

title = '날짜,종가,오픈,고가,저가,변동%'.split(',')
writer.writerow(title)

data_rows = soup.find('table', attrs={'class':'genTbl closedTbl historicalTbl'}).find('tbody').find_all('tr')
for row in data_rows:
    columns = row.find_all('td')
    if len(columns) <= 1: # 의미 없는 데이터 skip
        continue
    data = [column.get_text().strip() for column in columns]
    #print(data)
    writer.writerow(data)