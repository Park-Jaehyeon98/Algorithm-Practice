# -*- coding: utf-8 -*-
"""2_K번째 수.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCYbAeBVI-PJQS0Pj62iZkuKfZKNvzbH
"""

n = int(input())

for i in range(n):
    a, s, e, k = map(int, input().split())
    li = list(map(int, input().split()))
    sub_li = sorted(li[s-1:e])
    print("#%d %d" %(i+1, sub_li[k-1]))

