# -*- coding: utf-8 -*-
"""1966.숫자를 정렬하자

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r54ytHLqA-hJcAT1kQtTVjjMbMk5Ynjf
"""

t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{i} {' '.join(map(str, arr))}")