import requests
from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==============================================================================================================

# 0. 사이트 설정

print()
print('='*10,'프로그램이 실행됩니다.','='*10)
print()

print('사이트를 선택하세요.')
print()

site_name = ['인베스팅닷컴','통계청', 'FRED']
site_num = int(input('인베스팅닷컴 = 1, 통계청 = 2, FRED = 3\n\n입력 : ')) - 1
print()
print(site_name[site_num],'에서 자료를 추출합니다.')
num = int(site_num)

save_pathstr = '바탕화면'
save_path = r'C:\Users\pjk\desktop'

# ==============================================================================================================

# 1. 인베스팅닷컴

if site_num == 0:
    choose0 = {
        '코스피':'https://kr.investing.com/indices/kospi-historical-data',
        'snp500':'https://kr.investing.com/indices/us-spx-500-historical-data',
        '나스닥 100':'https://kr.investing.com/indices/nq-100-historical-data',
        '환율':'https://kr.investing.com/currencies/usd-krw-historical-data',
        '미국채 10년 만기 선물':'https://kr.investing.com/rates-bonds/us-10-yr-t-note-historical-data',
        '달러지수':'https://kr.investing.com/currencies/us-dollar-index-historical-data',
        '금선물':'https://kr.investing.com/commodities/gold-historical-data',
        '은선물':'https://kr.investing.com/commodities/silver-historical-data',
        'WTI원유':'https://kr.investing.com/commodities/crude-oil-historical-data',
        '비트코인':'https://kr.investing.com/crypto/bitcoin/btc-usd-historical-data'
    }
    print('='*100)

    print('검색 필터를 설정합니다.')
    print()
    term = input('자료 기간 설정을 위해 숫자를 입력해주세요 ex) 일간 = 1, 주간 = 2, 월간 = 3\n\n입력 : ')
    print()
    start_dt = input('시작일을 입력해 주세요 ex) 2010/1/31\n\n입력 : ')
    print()
    end_dt = input('종료일을 입력해 주세요 ex) 2020/1/31\n\n입력 : ')
    filter_set = [term, start_dt, end_dt]

    print('='*100)

    # 자료 검색

    print('[검색 목록]\n',list(choose0.keys())) # site_num 결과에 따라 choose숫자 변하도록 수
    print()
    t_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n각 대상은 쉼표(,)로 구분합니다. 예시) 금,코스피\n\n입력 : ').split(',')
    print()
    
    # 자료 형식 설정
    form = input('데이터 형식 xls, csv 중 하나를 정확히 입력하세요.\n\n입력 : ')

    for i, txt in enumerate(t_list):
        url = choose0[str(t_list[i])] # choose 수정
        print()
        print(t_list[i],'데이터 link : '.format(i + 1), url)

        # selenium
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #options.add_argument("no-sandbox")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(url)

        
        try: # 팝업창 닫기, 기간 선택  //*[@id="data_interval"]
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()
        except:
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="data_interval"]'))).click()
        else:
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="data_interval"]'))).click()
        
        # 일간,주간,월간 선택
        browser.find_element_by_xpath('//*[@id="data_interval"]/option[{}]'.format(filter_set[0])).click() # term : option[1] 일간, [2]주간, [3]월간
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
            
            print()
            print(t_list[i], '의 저장경로는 ', save_path, '입니다.')

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
        except: # 팝업 제거
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
            
            print()
            print(t_list[i], '의 저장경로는 ', save_path, '입니다.')

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
            print(t_list[i], '저장 됐습니다.')
            print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))
        else:
            print(t_list[i], '저장 됐습니다.')
            print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))

# ===============================================================================================================================================

# 2. 통계청

# 자료 주기 입력
elif site_num == 1:
    print('='*100)
    freq_input = int(input('자료의 주기를 선택해주세요.\n\n월 = 1, 분기 = 2, 반기 = 3, 연 = 4\n\n입력 : '))-1
    print()
    if freq_input == 0:
        freq = 'M'
        choose1 = {
                '시가총액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq={}'.format(freq),
                '외국인 증권 투자 현황ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq={}'.format(freq),
                '환율ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq={}'.format(freq),
                '외환보유액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq={}'.format(freq),
                '소비자물가상승률ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq={}'.format(freq),
                '통화량 추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq={}'.format(freq),
                '생산자물가지수ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq={}'.format(freq),
                '일반고용동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq={}'.format(freq),
                '주택매매가격 동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq={}'.format(freq),
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq={}'.format(freq),
                '경기종합지수m':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1057&stts_cd=105701&freq={}'.format(freq),
                '통화량추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq={}'.format(freq),
                '소비자심리지수m':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1058&stts_cd=105801&freq={}'.format(freq)
        }
    elif freq_input == 1:
        freq = 'Q'
        choose1 = {
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq={}'.format(freq),
                '석유화학분야 가격 동향yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq={}'.format(freq),
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq={}'.format(freq)
        }
    elif freq_input == 2:
        freq = 'H'
        choose1 = {
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq={}'.format(freq)
        }
    elif freq_input == 3:
        freq = 'Y'
        choose1 = {
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq={}'.format(freq),
                '시가총액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq={}'.format(freq),
                '외국인 증권투자 현황ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq={}'.format(freq),
                '환율ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq={}'.format(freq),
                '외환보유액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq={}'.format(freq),
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq={}'.format(freq),
                '소비자물가상승률ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq={}'.format(freq),
                '국가채무추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq={}'.format(freq),
                '출생 사망 추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1011&stts_cd=101101&freq={}'.format(freq),
                '통화량 추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq={}'.format(freq),
                '생산자물가지수ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq={}'.format(freq),
                '일반고용동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq={}'.format(freq),
                '석유화학분야 가격 동향yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq={}'.format(freq),
                '주택매매가격 동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq={}'.format(freq),
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq={}'.format(freq),
                '국가채무추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq={}'.format(freq),
                '통화량추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq={}'.format(freq),
                '합계출산율y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1428&stts_cd=142801&freq={}'.format(freq),
                '지니계수y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1407&stts_cd=140701&freq={}'.format(freq)
        }        
    else:        
        print('정확히 입력해 주세요.')
    
    # 검색 필터 입력
    
    print('='*100)
    
    print('<검색 가능 목록>\n\n',list(choose1.keys()))

    print()
    # selenium 사용.

    t_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요. 각 대상은 쉼표(,)로 구분합니다.\n예시) 시가총액ym,환율ym\n\n입력 : ').split(',')
    for i, txt in enumerate(t_list):
        url = choose1[str(t_list[i])]
        
        print('link : ',url,'\n{}번 자료를'.format(i + 1), save_pathstr,'에 저장합니다.')
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #options.add_argument("no-sandbox")
        options.add_argument("disable-gpu")
        options.add_argument("lang=ko_KR")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
        
        options.add_experimental_option("prefs", {
        "download.default_directory": save_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        })

        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(url)
        
        soup = BeautifulSoup(browser.page_source, 'lxml')

        if freq_input == 0:
            print(t_list[i],'의 검색 필터를 설정합니다.')
            print()
            ranges = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodS"]'))).text.split('\n')
            range_start = ranges[0]
            range_end = ranges[-1]
            print('검색 가능 기간 : ', range_start, ' 부터 ', range_end, ' 까지 ')
            print()
            start_dt2 = input('시작년월을 입력해 주세요 ex) 201001\n\n 입력 : ')
            print()
            end_dt2 = input('종료년월을 입력해 주세요 ex) 202001\n\n 입력 : ')
            filter_set2 = [start_dt2, end_dt2]

            # 월에서 기간 범위 선택
            try:
                elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodS"]')))
                elem.click()
                time.sleep(0.5)
                elem.send_keys(filter_set2[0])

                elem2 = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="periodE"]')))
                elem2.click()
                time.sleep(0.5)
                elem2.send_keys(filter_set2[1])
                
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
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))
                else:
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))

        # 나머지 기간은 전체 기간 다운로드
        else: 
            try: 
                browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/p/a/span').click() # 다운로드 버튼 클릭       
            except:
                print('에러')
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
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))
                else:
                    print('{} 중 {} 개가 완료됐습니다.'.format(len(t_list), i+1))
              
# ===================================================================================================================================        

# 3. FRED

else:
    urls = {
            '하이일드 채권 지수':'https://fred.stlouisfed.org/series/BAMLH0A0HYM2',
            '10년 채권 - 2년 채권':'https://fred.stlouisfed.org/series/T10Y2Y',
            '실업률':'https://fred.stlouisfed.org/series/UNRATE',
            '82년 100기준 소비자가격지수':'https://fred.stlouisfed.org/series/CPIAUCSL',
            '10-Year Treasury Inflation-Indexed Security':'https://fred.stlouisfed.org/series/DFII10',
            '10-Year Breakeven Inflation Rate':'https://fred.stlouisfed.org/series/T10YIE',
            '19년 3분기 1.381, 통화유통속도':'https://fred.stlouisfed.org/series/M2V',
            '11월 30일 18998, M2 통화량':'https://fred.stlouisfed.org/series/M2',
            'S&P 500':'https://fred.stlouisfed.org/series/SP500'
    }
    print('[데이터 목록]\n\n',list(urls.keys()))
    print()
    choice = int(input('지수 확인 = 1, 데이터 다운로드 = 2\n\n입력 : '))
    if choice == 1:
        keys = list(urls.keys())
        values = list(urls.values())
        print('='*100)
        curr_time = time.strftime('[%Y년 %m월 %d일 %H시 %M분 기준]\n')
        print(curr_time)  
        print('바탕화면에 저장됩니다.')
        print()
        f = open('C://Users//pjk//Desktop//indexcheck.csv', 'a', encoding='utf-8-sig', newline='') # newline 자동 줄바꿈 ''로 없앰
        writer = csv.writer(f)
        writer.writerow([curr_time])

        for i,url in enumerate(urls):
            url = urls[keys[i]]
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
            res = requests.get(url,headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, 'lxml')
            find = soup.find('span', attrs = {'class':'series-meta-observation-value'}).get_text().strip()
            print(keys[i],' : ',find)
            data = [keys[i], find]
            writer.writerow(data)
    else:
        t_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n각 대상은 쉼표(,)로 구분합니다. 예시) 실업률,S&P 500\n\n입력 : ').split(',')
        for i, url in enumerate(t_list):
            url = urls[str(t_list[i])] # choose 수정
            print()
            print(t_list[i],'데이터 link : '.format(i + 1), url)
        # for i,url in enumerate(t_list):
        #     keys = list(urls.keys())
        #     url = urls[keys[i]]
            browser = webdriver.Chrome()
            browser.maximize_window()
            browser.get(url)        
            startd = browser.find_element_by_xpath('//*[@id="input-cosd"]')
            startd.click()
            startd.clear()
            startd.send_keys('2006-01-02')
            time.sleep(1.5)
            endd = browser.find_element_by_xpath('//*[@id="input-coed"]')
            endd.click()
            endd.clear()
            endd.send_keys('2021-01-18')
            time.sleep(1.5)
            
            # 표 정보 수정
            browser.find_element_by_xpath('//*[@id="edit-graph-button"]/a[1]').click()
            time.sleep(1)

            # 빈도 수정 combobox 문제 해결!
            freq = browser.find_element_by_xpath('//*[@id="frequency-select"]')
            freq.click()
            selectEle = browser.find_element_by_id('frequency-select')
            selectEle.click()
            options=selectEle.find_elements_by_tag_name('option')
            for optionEle in options:
                if optionEle.text == 'Monthly':
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
    browser.quit()
    print('모든 과정이 완료됐습니다.\n5초 뒤 브라우저를 종료합니다.')
except:
    print('모든 과정이 완료됐습니다.\n프로그램을 종료합니다.')
else:
    time.sleep(5)  