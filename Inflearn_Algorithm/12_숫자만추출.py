# -*- coding: utf-8 -*-
"""12_숫자만추출

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQRjLomj3iAWsQEk4Vj63bS9pkZNFkLZ
"""

a = input()
num = ""
cnt = 0

for i in a:
    if i.isdigit():
        num += i

num = int(num)

for i in range(1, num+1):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)