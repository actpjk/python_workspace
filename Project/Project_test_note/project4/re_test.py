import re

p = re.compile('ca.s')

check = ['case','cafe','careless']

m = p.match(check)

print(m)