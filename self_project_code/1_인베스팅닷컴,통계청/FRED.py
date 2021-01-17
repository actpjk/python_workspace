import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# beautifulsoup
urls = {
'하이일드 채권 지수':'https://fred.stlouisfed.org/series/BAMLH0A0HYM2',
'10년 채권 minus 2년 채권':'https://fred.stlouisfed.org/series/T10Y2Y',
'실업률':'https://fred.stlouisfed.org/series/UNRATE',
'82년 100기준 소비자가격지수':'https://fred.stlouisfed.org/series/CPIAUCSL',
'BEI 기대인플레이션율':'https://fred.stlouisfed.org/series/T10YIE',
'10년물 국고채':'https://fred.stlouisfed.org/series/DGS10',
'10년물 실질이자율':'https://fred.stlouisfed.org/series/DFII10',
'19년 3분기 1.381, 통화유통속도':'https://fred.stlouisfed.org/series/M2V',
'11월 30일 18998, M2 통화량':'https://fred.stlouisfed.org/series/M2',
'SnP 500':'https://fred.stlouisfed.org/series/SP500'

}

keys = list(urls.keys())
values = list(urls.values())
print()
curr_time = time.strftime('%Y년 %m월 %d일 %H시 %M분 기준')
print()
print(curr_time)
f = open('G://files//selfproject//economic_data//FRED//today.csv', 'at', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
writer.writerow([curr_time])

for i,url in enumerate(urls):
        url = urls[keys[i]]
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
        res = requests.get(url,headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        find = soup.find('span', attrs = {'class':'series-meta-observation-value'}).get_text().strip()
        print(keys[i],' : ',find,'\nlink : ',values[i])
        data = [keys[i], find]
        writer.writerow(data)
time.sleep(20)
        # # 이미지 다운로드
        # li = soup.find_all('a')
        # print(li)
        # # down_list = ul.find_all('li')
        # # iamge_url_skip = down_list[2]['href']
        # # image_url = 'https://fred.stlouisfed.org/'+iamge_url_skip
        # # print(image_url)
        # # image_res = requests.get(image_url, headers=headers)
        # # image_res.raise_for_status()
        # # save_path_image = 'G://files//selfproject//economic data//FRED//{}_{}.png'.format(curr_time, keys[i])

        # # with open(save_path_image, 'wb') as f:
        # #     f.write(image_res.content)

        # selenium 1년치 그래프 이미지 다운로드 / 왜 계속 다운로드 실패하는거??

        # print('이미지 다운로드')
        # save_path = 'G://files//selfproject//economic_data//FRED'
        # options = webdriver.ChromeOptions()
        # #options.add_argument('headless')
        # #options.add_argument("no-sandbox")
        # options.add_argument("disable-gpu")
        # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
        # options.add_experimental_option("prefs", {
        # "download.default_directory": save_path,
        # "download.prompt_for_download": False,
        # "download.directory_upgrade": True,
        # "safebrowsing.enabled": True
        # })

        # browser = webdriver.Chrome(options=options)
        # browser.maximize_window()
        # browser.get(url)

        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="zoom-1yr"]'))).click()
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="download-button"]'))).click()
        # time.sleep(1)
        # WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="export-png"]'))).click()
        # time.sleep(4)
# browser.quit()
        




