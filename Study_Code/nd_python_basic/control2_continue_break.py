# continue & break

absent = [2, 5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue # 아래 있는 문장 진행시키지 않고 반복하게 함
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
        break # 바로 반복문 탈출
    print('{0}, 책을 읽어봐'.format(student))
