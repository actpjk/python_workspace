# 키워드값과 기본값

# def profile(name, age, main_lang):
#     print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'\
#         .format(name, age, main_lang))

# profile('유재석', 20, '파이썬')


# 같은 학교 같은 학년 같은 반 같은 수업.
# 이때 기본값이 필요

def profile(name, age=17, main_lang='파이썬'):
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'\
        .format(name, age, main_lang))
profile('유재석')
profile('김태호')
