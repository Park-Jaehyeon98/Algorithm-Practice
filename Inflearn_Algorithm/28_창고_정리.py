# -*- coding: utf-8 -*-
"""28_창고 정리

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZX-EkRZWlBM-WvtjJG5kYW8Ml6e_rQcG
"""

n = int(input())
li = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    li.sort()
    li[-1] -= 1
    li[0] += 1

print(max(li) - min(li))