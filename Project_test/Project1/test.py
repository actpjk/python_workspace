def urls(site):      
    if site == 0:
        select = {
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
        return select

    elif site == 1:
        freq_input = int(input('자료의 주기를 선택해주세요.\n\n월 = 1, 분기 = 2, 반기 = 3, 연 = 4\n\n입력 : ')) - 1
        if freq_input == 0:
            select = {
                '시가총액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq=M',
                '외국인 증권 투자 현황ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq=M',
                '환율ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq=M',
                '외환보유액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq=M',
                '소비자물가상승률ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq=M',
                '통화량 추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=M',
                '생산자물가지수ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq=M',
                '일반고용동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq=M',
                '주택매매가격 동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq=M',
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=M',
                '경기종합지수m':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1057&stts_cd=105701&freq=M',
                '통화량추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=M',
                '소비자심리지수m':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1058&stts_cd=105801&freq=M'
            }
            return select, freq_input
        elif freq_input == 1:
            select = {
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Q',
                '석유화학분야 가격 동향yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq=Q',
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=Q'
            }
            return select, freq_input
        elif freq_input == 2:
            select = {
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=H'
            }
            return select, freq_input
        else:
            select = {
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Y',
                '시가총액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1079&stts_cd=107901&freq=Y',
                '외국인 증권투자 현황ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1086&stts_cd=108601&freq=Y',
                '환율ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1068&stts_cd=106801&freq=Y',
                '외환보유액ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1067&stts_cd=106701&freq=Y',
                '국내총샌산 및 경제성장률yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=2736&stts_cd=273601&freq=Y',
                '소비자물가상승률ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1060&stts_cd=106001&freq=Y',
                '국가채무추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq=Y',
                '출생 사망 추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1011&stts_cd=101101&freq=Y',
                '통화량 추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=Y',
                '생산자물가지수ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1061&stts_cd=106103&freq=Y',
                '일반고용동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1494&stts_cd=149406&freq=Y',
                '석유화학분야 가격 동향yq':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1144&stts_cd=114401&freq=Y',
                '주택매매가격 동향ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1240&stts_cd=124001&freq=Y',
                '수출입 동향yhqm':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1066&stts_cd=106601&freq=Y',
                '국가채무추이y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1106&stts_cd=110601&freq=Y',
                '통화량추이ym':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1072&stts_cd=107201&freq=Y',
                '합계출산율y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1428&stts_cd=142801&freq=Y',
                '지니계수y':'https://www.index.go.kr/potal/stts/idxMain/selectPoSttsIdxSearch.do?idx_cd=1407&stts_cd=140701&freq=Y'
            }
            return select, freq_input
def save_path():
    save_location = '바탕화면'
    save_path = r'C:\Users\pjk\desktop'
    return save_location, save_path

def freq_inv():
    print('검색 필터를 설정합니다.')
    print()
    term = input('자료 기간 설정을 위해 숫자를 입력해주세요 ex) 일간 = 1, 주간 = 2, 월간 = 3\n\n입력 : ')
    print()
    start_dt = input('시작일을 입력해 주세요 ex) 2010/1/31\n\n입력 : ')
    print()
    end_dt = input('종료일을 입력해 주세요 ex) 2020/1/31\n\n입력 : ')
    filter_set = [term, start_dt, end_dt]
    return filter_set

def  freq_fred():
    print('검색 필터를 설정합니다.\n')
    term = int(input('자료 기간 설정을 위해 숫자를 입력해주세요 ex) 일 = 1, 월 = 2, 분기 = 3, 연 = 4\n\n입력 : ')) - 1
    start_dt = input('시작일을 입력해 주세요 ex) 2010/1/31\n\n입력 : ')
    end_dt = input('종료일을 입력해 주세요 ex) 2020/1/31\n\n입력 : ')
    filter_set = [term, start_dt, end_dt]
    return filter_set    

def search():
    print('[검색 목록]\n\n', select[0].keys(),'\n')
    search_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n각 대상은 쉼표(,)로 구분합니다. 예시) 금,실업률\n\n입력 : ').split(',')
    form = input('데이터 형식 xlsx, csv 중 하나를 정확히 입력하세요.\n\n입력 : ')
    return search_list, form

def search_fred():
    view = int(input('지수 확인 = 1, 데이터 다운로드 = 2\n\n입력 : '))
    print('[검색 목록]\n\n', select[0].keys(),'\n')
    if view == 2:
        search_list = input('목록의 작은 따옴표 내 검색할 대상을 똑같이 입력해 주세요.\n각 대상은 쉼표(,)로 구분합니다. 예시) 금,실업률\n\n입력 : ').split(',')
        form = input('데이터 형식 xlsx, csv 중 하나를 정확히 입력하세요.\n\n입력 : ')
    else:
        print('지수 확인')
    return view, search_list, form

select = urls(1)
print(select)

data_freq = select[1]
search = search()
search_list = list(search[0]) # 입력한 search_list
form = search[1]
select_dict = select[0]
#print(select) # -> 튜플임
print(select_dict[select[0]])


