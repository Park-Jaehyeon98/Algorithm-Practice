# -*- coding: utf-8 -*-
"""5_정다면체.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11nnwFSVlTZx78Dt3dIpJhPL77EWdyqOq
"""

n, m = map(int, input().split())

max = 0
a = [0] * (n+m+2)

for i in range(1, n+1):
    for j in range(1, m+1):
        a[i+j] += 1

for i in range(n+m+1):
    if a[i] > max:
        max = a[i]

for i in range(n+m+1):
    if a[i] == max:
        print(i, end=' ')