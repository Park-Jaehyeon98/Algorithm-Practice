# -*- coding: utf-8 -*-
"""9_주사위 게임

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q-FpdpwXJFm7OG8Sv0OLeUCTYolTyGpP
"""

n = int(input())
li = []

for i in range(n):
    a, b, c = map(int, input().split())
    sum = 0
    if a == b and b == c:
        li.append(10000 + a * 1000)
    elif a == b or a == c:
        li.append(1000 + a * 100)
    elif b == c:
        li.append(1000 + b * 100)
    else:
        li.append(max(a, b, c) * 100)

print(max(li))