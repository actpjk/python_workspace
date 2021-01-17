# 모듈 사용 실습

import sys

print(sys)
print(type(sys.path))


# 모듈 경로 삽입

sys.path.append('C:/math') # -> 영구적으로 등록되는게 아님.

print(sys.path)

import test_module

print(test_module.power(10,3 ))
