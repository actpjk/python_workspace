# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(str)

# 예제1

#name = input("Enter your name")
#grade = input("Enter your Grade")
#company = input('Enter your company name')

#print(name, grade, company)

# 예제2

number = input("Enter number : ")
name = input('Enter name')

print('type of number', type(number))
print('type of name', type(name))


# 예제 3(계산)
# first_number = int(input('Enter number1 : '))
# second_number = int(input('Enter number2 : '))
#
# total =  first_number + second_number
# print('first_number + second_number : ', total)


#예제 4

float_number = float(input('Enter a float number : '))

print('input float :', float_number * 2.1719)
print('input type :', type(float_number))


# 예제5

print('FirstName - {0}, LastName - {1}'.format(input('Enter First name : '), input('Enter Second name : ')))
