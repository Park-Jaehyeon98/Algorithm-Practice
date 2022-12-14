# -*- coding: utf-8 -*-
"""29_ 침몰하는 타이타닉(그리디)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DkQ7Xg1eF4cIjI-exTUfHg5nNKQOR56R
"""

from collections import deque

n, m = map(int, input().split())
li = list(map(int, input().split()))

cnt = 0
li.sort()
dq = deque(li)

while dq:
    if len(dq)==1:
        cnt += 1
        break
    if dq[0] + dq[-1] > m:
        dq.pop()
        cnt += 1
    else:
        dq.popleft()
        dq.pop()
        cnt += 1

print(cnt)