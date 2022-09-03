# -*- coding: utf-8 -*-
"""32_가장 큰 수

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9Tu3ojBOtRTiaSzYrra3L0bbxtIFGq7
"""

num, n = map(int, input().split())
num = list(map(int, str(num)))

a = []

for i in num:
    while a and n > 0 and a[-1] < i:
        a.pop()
        n -= 1
    a.append(i)

if n != 0:
    a = a[:-n]

result = ''.join(map(str, a))
print(result)