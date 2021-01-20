# 가변인자

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = '유재석', main_lang = '파이썬', age = 20)
# profile(main_lang = '자바',name = '김태호' , age = 20) # 순서가 뒤섞여 있어도 호출 가능

# def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
#     print('이름 : {0}\t나이 : {1}\t'.format(name, age), end='') # end = '' : 밑 문장을 한 줄로 이어서 계속 출력 
#     print(lang1, lang2, lang3, lang4, lang5)

# profile2('유재석', 20, 'python', '자바', 'c+', 'c++', 'c#')
# profile2('김태호', 20, 'python', '코틀린','','','')

def profile3(name, age, *language): # 가변 인자
    print('이름 : {0}\t나이 : {1}\t'.format(name, age), end='')
    for lang in language:
        print(lang, end=' ')
    print()

profile3('유재석', 20, 'python', '자바', 'c+', 'c++', 'c#','파스타')
profile3('김태호', 20, 'python', '코틀린')