from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# class extraction:
#     def __init__ (self, url, save_dir, id, pw, term, start_dt, end_dt, file_name):
#         self.url = url
#         self.save_directory = save_dir
#         self.id = id
#         self.pw = pw
#         self.term = term
#         self.start_date = start_dt
#         self.end_date = end_dt
#         self.file_name = file_name
print('데이터 사이트를 선택하세요.')
site_name = ['https://kr.investing.com', 'koreabank', 'koreastatic', 'FRED']
# site_list2 = ['investing', 'koreabank', 'koreastatic', 'FRED']
site_num = int(input('인베스팅닷컴 = 1, 한국은행 = 2, 통계청 = 3, FRED = 4\n입력 : ')) - 1

if site_num == 0:
    choose0 = {
        '코스피':'https://kr.investing.com/indices/kospi',
        'snp500':'https://kr.investing.com/indices/us-spx-500',
        '나스닥 100':'https://kr.investing.com/indices/nq-100',
        '원/달러 환율':'https://kr.investing.com/currencies/usd-krw',
        '미국채 10년 만기 선물':'https://kr.investing.com/rates-bonds/us-10-yr-t-note',
        '달러지수':'https://kr.investing.com/currencies/us-dollar-index',
        '금':'https://kr.investing.com/commodities/gold',
        '은':'https://kr.investing.com/commodities/silver',
        'WTI원유':'https://kr.investing.com/commodities/crude-oil',
        '비트코인':'https://kr.investing.com/crypto/bitcoin/btc-usd'
    }
    print(site_name[site_num], '에서 csv자료를 scraping합니다.')

elif site_num == 1:
    print('Not Yet, 준비중입니다.')
    pass
elif site_num == 2:
    print('Not Yet, 준비중입니다.')
    pass
else:
    print('Not Yet, 준비중입니다.')
    pass

print('='*100)

# 
# input('비밀번호를 입력하세요 : ')

id = input('비밀번호는 저장되어 있습니다.\n인베스팅닷컴 아이디 주소만 입력하세요\n\n입력 : ')
pw = 'rhkdqhrwjf9384@'
personal = [id, pw]

print('='*100)

print('검색 필터를 설정합니다.')
print()
term = input('자료 기간 설정을 위해 숫자를 입력해주세요 ex) 일간 = 1, 주간 = 2, 월간 = 3\n입력 : ')
start_dt = '2010/1/1' # input 설정하기
end_dt = '2020/1/1'
filter_set = [term, start_dt, end_dt]

print('='*100)

print('[검색 목록]\n', list(choose0.keys()))
t_list = input('목록의 작은 따옴표 내 검색할 대상을 띄어쓰기까지 정확히 입력해 주세요.\n각 대상은 쉼표+띄어쓰기(, )로 구분합니다.\n입력 : ').split(', ')
for i, txt in enumerate(t_list):
    url = choose0[str(t_list[i])]
    print('{}번 사이트 주소 : '.format(i + 1), url)
    # 저장 경로 지정
    save_path = r'C:\Users\pjk\Desktop\data'
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument("no-sandbox")
    options.add_argument('window-size=600x400')
    options.add_argument("disable-gpu")
    options.add_argument("lang=ko_KR")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
    options.add_experimental_option("prefs", {
    "download.default_directory": save_path, # save_path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 로그인 (버튼으로 만들기), 팝업창 닫기
    try:   
        browser.find_element_by_xpath('//*[@id="PromoteSignUpPopUp"]/div[2]/i').click()
    except:
        browser.find_element_by_xpath('//*[@id="userAccount"]/div/a[1]').click()
    else:
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="userAccount"]/div/a[1]').click()
    

    browser.find_element_by_id('loginFormUser_email').send_keys(personal[0])
    browser.find_element_by_id('loginForm_password').send_keys(personal[1])
    browser.find_element_by_xpath('//*[@id="signup"]/a').click() 

    browser.find_element_by_link_text('과거 데이터').click()

    # 기간의 단위 선택
    # term = cmb_term.get()
    # browser.find_element_by_id('data_interval').click()
    browser.find_element_by_xpath('//*[@id="data_interval"]/option[{}]'.format(filter_set[0])).click() # term : [1]일간, [2]주간, [3]월간

    # 기간의 범위 선택
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="widgetFieldDateRange"]'))).click() 

    start_date = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startDate"]')))
    start_date.click()
    start_date.clear()
    start_date.send_keys(filter_set[1]) # start_dt

    end_date = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endDate"]')))
    end_date.click()
    end_date.clear()
    end_date.send_keys(filter_set[2]) # end_dt
    browser.find_element_by_xpath('//*[@id="applyBtn"]').click()
    time.sleep(1.5)

    # 다운로드 버튼 클릭
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-content"]/div[4]/div/a'))).click()
    
    # 저장된 파일 이름 확인
    file_name = soup.find('h2', attrs={'class':'float_lang_base_1 inlineblock'}).get_text()
    print(file_name, '저장 됐습니다.')
    print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))

print('모든 과정이 완료됐습니다.\n브라우저를 종료합니다.')
time.sleep(3)
browser.quit()
