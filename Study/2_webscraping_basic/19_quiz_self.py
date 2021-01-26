import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0'
browser.get(url)
elem = browser.find_element_by_xpath('//*[@id="estateCollInnerTab"]/div/span[2]/a')
elem.click()

soup = BeautifulSoup(browser.page_source, 'lxml')

houses = soup.find('div', attrs = {'class':'wrap_tbl tbl_trade'}).find('tbody').find_all('tr')

print('[출력 결과]')

for idx, house in enumerate(houses):
    
    typ =  house.find('td', attrs = {'class':'col1'}).get_text()
    area = house.find('td', attrs = {'class':'col2'}).get_text()
    price = house.find('td', attrs = {'class':'col3'}).get_text()
    dong = house.find('td', attrs = {'class':'col4'}).get_text()
    level = house.find('td', attrs = {'class':'col5'}).get_text()
    
    print('='*10, f'매물 {idx + 1}','='*10)
    print(f'거래 : {typ}')
    print(f'면적 : {area} (공급/전용)')
    print(f'가격 : {price} (만원)')
    print(f'동 : {dong}')
    print(f'층 : {level}')

