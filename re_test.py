import re

with open('/Users/chenhuigu/Documents/GitHub/relat_extra/re_test.txt') as f:
    content = f.read()
list = re.findall(r'.*基本每股收益.*', content)
print(list)