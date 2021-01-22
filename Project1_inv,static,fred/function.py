# library import

import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =============================================================================================================================================================================        

# 함수 (인베스팅 : 0, 통계청 : 1, FRED : 2 or else)

def urls(site):      
    if site == 0:
        select = {
            '코스피':'https://kr.investing.com/indices/kospi-historical-data',
            'snp500':'https://kr.investing.com/indices/us-spx-500-historical-data',
            '나스닥100':'https://kr.investing.com/indices/nq-100-historical-data',
            '환율':'https://kr.investing.com/currencies/usd-krw-historical-data',
            '미국채 10년 만기 선물':'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data',
            '달러지수':'https://kr.investing.com/currencies/us-dollar-index-historical-data',
            '금':'https://kr.investing.com/commodities/gold-historical-data',
            '은':'https://kr.investing.com/commodities/silver-historical-data',
            'WTI원유':'https://kr.investing.com/commodities/crude-oil-historical-data',
            '비트코인':'https://kr.investing.com/crypto/bitcoin/btc-usd-historical-data'
        }
        return select

    elif site == 1:
        print('='*100)
        print('\n검색 필터를 설정합니다.\n')
        term = int(input('자료의 주기를 선택해주세요.\n\n월 = 1, 분기 = 2, 반기 = 3, 연 = 4\n\n입력 : ')) - 1
        if term == 0:
            select = {
                '시가총액':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq=M',
                '외국인 증권 투자 현황':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq=M',
                '환율':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq=M',
                '외환보유액':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq=M',
                '소비자물가상승률':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq=M',
                '통화량 추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=M',
                '생산자물가지수':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq=M',
                '일반고용동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq=M',
                '주택매매가격 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq=M',
                '수출입 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=M',
                '경기종합지수':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1057&stts_cd=105701&freq=M',
                '통화량추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=M',
                '소비자심리지수':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1058&stts_cd=105801&freq=M'
            }
            return select, term
        elif term == 1:
            select = {
                '국내총샌산 및 경제성장률':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Q',
                '석유화학분야 가격 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq=Q',
                '수출입 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=Q'
            }
            return select, term
        elif term == 2:
            select = {
                '수출입 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=H'
            }
            return select, term
        else:
            select = {
                '국내총샌산 및 경제성장률':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Y',
                '시가총액':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq=Y',
                '외국인 증권투자 현황':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq=Y',
                '환율':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq=Y',
                '외환보유액':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq=Y',
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Y',
                '소비자물가상승률':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq=Y',
                '국가채무추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq=Y',
                '출생 사망 추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1011&stts_cd=101101&freq=Y',
                '통화량 추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=Y',
                '생산자물가지수':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq=Y',
                '일반고용동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq=Y',
                '석유화학분야 가격 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq=Y',
                '주택매매가격 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq=Y',
                '수출입 동향':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=Y',
                '국가채무추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq=Y',
                '통화량추이':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=Y',
                '합계출산율':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1428&stts_cd=142801&freq=Y',
                '지니계수':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1407&stts_cd=140701&freq=Y'
            }
            term = 3
            return select, term
    else:
        select = {
            '하이일드 채권':'https://fred.stlouisfed.org/series/BAMLH0A0HYM2',
            '10년 채권 - 2년 채권':'https://fred.stlouisfed.org/series/T10Y2Y',
            '실업률':'https://fred.stlouisfed.org/series/UNRATE',
            '소비자가격지수':'https://fred.stlouisfed.org/series/CPIAUCSL',
            '실질금리':'https://fred.stlouisfed.org/series/DFII10',
            '기대인플레이션율':'https://fred.stlouisfed.org/series/T10YIE',
            '통화유통속도':'https://fred.stlouisfed.org/series/M2V',
            'M2':'https://fred.stlouisfed.org/series/M2',
            'S&P 500':'https://fred.stlouisfed.org/series/SP500'
        }
        return select

def freq():
    
    if site_num = 1:
        pass
    else:
        print('\n검색 필터를 설정합니다.\n')
        term = int(input('자료 기간 설정을 위해 숫자를 입력해주세요 ex) 일간 = 1, 주간 = 2, 월간 = 3\n\n입력 : ')) - 1
        print()
        start_dt = input('시작일을 입력해 주세요 ex) 2010/1/31\n\n입력 : ')
        print()
        end_dt = input('종료일을 입력해 주세요 ex) 2020/1/31\n\n입력 : ')
        form = input('\n데이터 형식 xlsx, csv 중 하나를 정확히 입력하세요.\n\n입력 : ')
        filter_set = [term, start_dt, end_dt]
        return filter_set, form

def search():
    if site_num == 0 or site_num == 2:
        print('\n[검색 목록]\n\n', list(select.keys()),'\n')
        search_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n\n각 대상은 쉼표(,)로 구분합니다.\n\n예시) 금,실업률\n\n입력 : ').split(',')
        return search_list         
    elif site_num == 1:
        print('\n[검색 목록]\n\n', list(select[0].keys()),'\n')
        search_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n\n각 대상은 쉼표(,)로 구분합니다.\n\n예시) 금,실업률\n\n입력 : ').split(',')
        return search_list        
    else: # FRED Data의 경우 print 함수를 이용한 체크 기능, 데이터 다운로드 기능 2개
        view = int(input('지수 확인 = 1, 데이터 다운로드 = 2\n\n입력 : '))
        if view == 1:
            print('지수만 확인합니다.')
            return view
        else:
            print('\n[검색 목록]\n\n', list(select.keys()),'\n')
            search_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n\n각 대상은 쉼표(,)로 구분합니다.\n\n예시) 금,실업률\n\n입력 : ').split(',')
            return view, search_list
        
# =============================================================================================================================================================================        

# 0. 초기 설정

# try:
print('\n','='*10,'프로그램이 실행됩니다.','='*10,'\n')
print('사이트를 선택하세요.\n')
site_name = ['인베스팅닷컴','통계청', 'FRED']
site_num = int(input('인베스팅닷컴 = 1, 통계청 = 2, FRED = 3\n\n입력 : ')) - 1
print('\n',site_name[site_num],'에서 자료를 추출합니다.\n')

select = urls(site_num) # url 주소

save_name = '바탕화면'
save_path = r'C:\Users\pjk\desktop'

options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument("no-sandbox")
options.add_argument("disable-gpu")
if site_num == 0 or 1:
    options.add_argument("lang=ko_KR")
else:
    pass
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36  \
    (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
options.add_experimental_option("prefs", {
"download.default_directory": save_path,
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True
})


# =============================================================================================================================================================================        

# 1. 인베스팅닷컴

if site_num == 0:

    # 자료 검색
    filter_set = freq()
    search = search()
    search_list = search[0] # 입력한 search_list
    form = freq[1] # 데이터 형식

    for i, txt in enumerate(search_list):
        url = select[str(search_list[i])]
        print()
        print(search_list[i], '데이터 link : '.format(i + 1), url)

        # selenium
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(url)

        try: # 팝업창 닫기, 기간 클릭  //*[@id="data_interval"]
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()
        except:
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="data_interval"]'))).click()
        else:
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="data_interval"]'))).click()
        
        # 일간,주간,월간 선택
        browser.find_element_by_xpath('//*[@id="data_interval"]/option[{}]'.format(filter_set[0]+1)).click() # term : option[1] 일간, [2]주간, [3]월간
        time.sleep(1)

        # 달력 버튼 옆 자료 범위 선택
        try: 
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="widgetFieldDateRange"]'))).click() # 달력 버튼 클릭

            start_date = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startDate"]')))
            start_date.click()
            start_date.clear()
            start_date.send_keys(filter_set[1]) # 시작일자

            end_date = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endDate"]')))
            end_date.click()
            end_date.clear()
            end_date.send_keys(filter_set[2]) # 종료일자

            browser.find_element_by_xpath('//*[@id="applyBtn"]').click() # 신청합니다 클릭

            time.sleep(1)
            
            # title, data, 저장 경로 추가
            soup = BeautifulSoup(browser.page_source, 'lxml')
            file_name = soup.find('h2', attrs={'class':'float_lang_base_1 inlineblock'}).get_text().replace('/','_')
            save_path = 'C://Users//pjk//desktop//{}.{}'.format(file_name, form)
            
            print('\n',search_list[i], '의 저장경로는 ', save_path, '입니다.')

            # 제목
            f = open(save_path, 'w', encoding='utf-8-sig', newline='')
            writer = csv.writer(f)
            titles = soup.find('table', attrs={'class':'genTbl closedTbl historicalTbl'})
            title = titles.find('tr').get_text().strip().split('\n')
            if title[5] == '거래량 변동 %':
                del title[-1]
                title[6:7] = ['거래량', '변동 %']
            else:
                pass
            writer.writerow(title)

            # 내용
            data_rows = soup.find('table', attrs={'class':'genTbl closedTbl historicalTbl'}).find('tbody').find_all('tr')
            for row in data_rows:
                columns = row.find_all('td')
                if len(columns) <= 1: # 의미 없는 데이터 skip
                    continue
                data = [column.get_text().strip() for column in columns]
                writer.writerow(data)

        except: # try 오류시 팝업 제거 후 동일 시행
            # 팝업 제거
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()

            start_date = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="startDate"]')))
            start_date.click()
            start_date.clear()
            start_date.send_keys(filter_set[1]) # 시작일자

            end_date = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="endDate"]')))
            end_date.click()
            end_date.clear()
            end_date.send_keys(filter_set[2]) # 종료일자

            browser.find_element_by_xpath('//*[@id="applyBtn"]').click() # 신청합니다 클릭

            time.sleep(1)
            
            # title, data, 저장 경로 추가
            soup = BeautifulSoup(browser.page_source, 'lxml')
            file_name = soup.find('h2', attrs={'class':'float_lang_base_1 inlineblock'}).get_text().replace('/','_')
            save_path = 'C://Users//pjk//desktop//{}.{}'.format(file_name, form)
            
            print('\n\n',search_list[i], '의 저장경로는 ', save_path, '입니다.\n\n')

            f = open(save_path, 'w', encoding='utf-8-sig', newline='')
            writer = csv.writer(f)
            titles = soup.find('table', attrs={'class':'genTbl closedTbl historicalTbl'})
            title = titles.find('tr').get_text().strip().split('\n')
            if title[5] == '거래량 변동 %':
                del title[-1]
                title[6:7] = ['거래량', '변동 %']
            else:
                pass

            writer.writerow(title)
            data_rows = soup.find('table', attrs={'class':'genTbl closedTbl historicalTbl'}).find('tbody').find_all('tr')
            for row in data_rows:
                columns = row.find_all('td')
                if len(columns) <= 1: # 의미 없는 데이터 skip
                    continue
                data = [column.get_text().strip() for column in columns]
                writer.writerow(data)
            print('\n\n',search_list[i], '저장 됐습니다.\n')
            print('{} 중 {} 개가 완료됐습니다.\n'.format(len(search_list), i+1))
        else:
            print(search_list[i], '저장 됐습니다.\n')
            print('{} 중 {} 개가 완료됐습니다.\n'.format(len(search_list), i+1))

# =============================================================================================================================================================================        

# 2. 통계청

elif site_num == 1:
    print('\n','='*100)
    # select = urls(site_num) -> return select, term
    # 자료 검색
    select = select[0] # tuple 형태 
    term = select[1]
    
    soup = BeautifulSoup(browser.page_source, 'lxml')

    ranges = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodS"]'))).text.split('\n')
    range_start = ranges[0]
    range_end = ranges[-1]
    print('검색 가능 기간 : ', range_start, ' 부터 ', range_end, ' 까지 ')
    print()
    start_dt = input('시작일을 입력해 주세요 ex) 2010/1/31\n\n입력 : ')
    print()
    end_dt = input('종료일을 입력해 주세요 ex) 2020/1/31\n\n입력 : ')
    form = input('\n데이터 형식 xlsx, csv 중 하나를 정확히 입력하세요.\n\n입력 : ')
    filter_set = [start_dt, end_dt, term]

    search = search()
    search_list = search[0]

    for i, txt in enumerate(search_list):
        url = select_dict[txt]
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(url)
        if term == 0: # 월
            # 월에서 기간 범위 선택
            try:
                elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodS"]')))
                elem.click()
                time.sleep(0.5)
                elem.send_keys(filter_set[0]) # 시작일

                elem2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodE"]')))
                elem2.click()
                time.sleep(0.5)
                elem2.send_keys(filter_set[1]) # 종료일
                
                browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/span[3]/a').click() # 조회 버튼 클릭
                time.sleep(1)
                
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/p/a/span'))).click() # 다운로드 버튼 클릭
            except:
                print('에러 발생')
            else:
                try:
                    file_names = soup.find_all('option', attrs={'selected':'selected'}).get_text().strip()
                    file_name = file_names[0]
                    print(file_name, '데이터가 저장 됐습니다.')
                except:
                    file_name = soup.find('option', attrs={'selected':'selected'}).get_text().strip()
                    print(file_name, '데이터가 저장 됐습니다.')
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(search_list), i+1))
                else:
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(search_list), i+1))

        # 나머지 기간은 전체 기간 다운로드
        else: 
            try: 
                browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/p/a/span').click() # 다운로드 버튼 클릭       
            except:
                print('에러 발생')
            else: # 파일명이 여러개일 경우 발생하는 에러 방지
                try:
                    file_names = soup.find_all('option', attrs={'selected':'selected'}).get_text().strip()
                    file_name = file_names[0]
                    print('='*100)
                    print(file_name, '데이터가 저장 됐습니다.')
                except:
                    file_name = soup.find('option', attrs={'selected':'selected'}).get_text().strip()
                    print('='*100)
                    print(file_name, '데이터가 저장 됐습니다.')
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(search_list), i+1))
                else:
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(search_list), i+1))
            
# =============================================================================================================================================================================        

# 3. FRED

# 데이터 주기 확인 후
else:
    search = search()
    view = search[0]

    if view == 1:
        keys = list(select.keys())
        values = list(select.values())
        print('='*100)
        curr_time = time.strftime('[%Y년 %m월 %d일 %H시 %M분 기준]\n')
        print(curr_time)  
        print('바탕화면에 저장됩니다.')
        print()
        f = open('C://Users//pjk//Desktop//indexcheck.csv', 'a', encoding='utf-8-sig', newline='') # newline 자동 줄바꿈 ''로 없앰
        writer = csv.writer(f)
        writer.writerow([curr_time])

        for i,url in enumerate(select):
            url = select[keys[i]]
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
            res = requests.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
            find = soup.find('span', attrs = {'class':'series-meta-observation-value'}).get_text().strip()
            print(keys[i],' : ',find)
            data = [keys[i], find]
            writer.writerow(data)
            
    else: # view == 2
        search_list = search[1]
        form = freq[1]
        filter_set = freq[0]
        date_term = ['Daily', 'Mothly', 'Quaterly', 'Annual']

        for i, url in enumerate(search_list):
            url = select[str(search_list[i])]
            print('\n',search_list[i],'데이터 link : ', url)
            browser = webdriver.Chrome(options=options)
            browser.maximize_window()
            browser.get(url)        
            startd = browser.find_element_by_xpath('//*[@id="input-cosd"]')
            startd.click()
            startd.clear()
            time.sleep(1)
            startd.send_keys(filter_set[1])
            time.sleep(1)
            endd = browser.find_element_by_xpath('//*[@id="input-coed"]')
            endd.click()
            endd.clear()
            endd.send_keys(filter_set[2])
            time.sleep(1)
            
            # 표 정보 수정
            browser.find_element_by_xpath('//*[@id="edit-graph-button"]/a[1]').click()
            time.sleep(1)

            # 표 내 빈도 수정
            freq_chart = browser.find_element_by_xpath('//*[@id="frequency-select"]')
            freq_chart.click()
            selectEle = browser.find_element_by_id('frequency-select')
            selectEle.click()
            options=selectEle.find_elements_by_tag_name('option')
            for optionEle in options:
                if optionEle.text == date_term[filter_set[0]]:
                    optionEle.click()
                    break

            # 표 수정창 닫기
            browser.find_element_by_xpath('//*[@id="tabs-with-dropdown"]/div[1]/header/div[2]/a').click()
            time.sleep(1)
            
            # 다운로드
            browser.find_element_by_xpath('//*[@id="download-button"]').click()
            time.sleep(1)     
            browser.find_element_by_xpath('//*[@id="download-data-csv"]').click()
            

# for 반복문 완료 후 종료
print('='*100)    
try:
    print('\n모든 과정이 완료됐습니다.\n\n브라우저를 종료합니다.')
    time.sleep(5)
except:
    print('\n모든 과정이 완료됐습니다.\n\n브라우저를 종료합니다.')
    time.sleep(5)
    browser.quit()
else:
    browser.quit()
# except:
#     print('정확한 값을 입력하세요.')