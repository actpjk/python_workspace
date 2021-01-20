# 외장함수

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob('*.py')) # 확장자가 py 인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시

# folder = 'sample_dir'

# if os.path.exists(folder):
#     print('이미 존재하는 폴더 입니다.')
#     os.rmdir(folder)
#     print(folder, '폴더 삭제 완료')
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, '폴더를 생성하였습니다.')

# print(os.listdir())

# 시간 관련 

import time
print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime
print('오늘 날짜는', datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=200)
print('100일 후', today + td)