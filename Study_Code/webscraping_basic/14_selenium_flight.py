
from selenium import webdriver

# 로딩 기다리기
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = 'https://flight.naver.com/flights/'
browser.get(url) # url 이동

browser.find_element_by_link_text('가는날 선택').click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
# browser.find_elements_by_link_text('28')[0].click() # [0] -> 이번달

# browser.find_elements_by_link_text('27')[1].click() # [1] -> 다음달
# browser.find_elements_by_link_text('28')[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택

browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
browser.find_elements_by_link_text('28')[1].click() # [0] -> 다음달

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

# 브라우저 최대 10초 대기, xpath 기준 해당 element가 나올 때 까지
try: 
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')))
    # 성공시 동작 수행
    print(elem.text) # 첫 번째 결과 출력
finally:
    browser.quit()

# 첫 번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)