# with

import pickle

with open('profile.pickle', 'rb') as profile_file:
    print(pickle.load(profile_file)) # close 종료문 필요없이 자동 탈출

with open('study.txt', 'w', encoding='utf-8') as study_file:
    study_file.write('공부중입니다.')

with open('study.txt', 'r', encoding='utf-8') as study_file:
    print(study_file.read())