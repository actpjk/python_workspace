from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import re
import os
import numpy as np
from IPython.display import set_matplotlib_formats
import time

set_matplotlib_formats('retina')
plt.rc('font', family = 'Malgun Gothic')
plt.rc('axes', unicode_minus = False)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

url = 'https://opendart.fss.or.kr/api/list.xml'

report_type = {
    '사업보고서':'A001',
    '반기보고서':'A002',
    '분기보고서':'A003',
}

params = {
    'crtfc_key' : '31718c7bf232574ee78e6f3f81c922043baad322',
    'corp_code' : '032830',
    'bgn_de' : '19990101',
    'pblntf_detail_ty': '{}'.format(report_type['분기보고서']),
    'page_count': '100',
}

res = requests.get(url, headers = headers, params=params)
res.raise_for_status()

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://opendart.fss.or.kr/api/list.xml?crtfc_key=31718c7bf232574ee78e6f3f81c922043baad322&corp_code=032830&bgn_de=19990101&pblntf_detail_ty=A003&page_count=100')
time.sleep(2)
elem = browser.find_element_by_xpath('//*[@id="folder1"]/div[2]/div[6]/span[2]').text
print(elem)

