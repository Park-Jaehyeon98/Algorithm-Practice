# -*- coding: utf-8 -*-
"""21_격자판 회문수

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OX4DLk2afX0DfPfI3JOH8Rw64GcNGm7H
"""

li = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(7):
    for j in range(2, 5):
        if li[i][j-2] == li[i][j+2] and li[i][j-1] == li[i][j+1]:
            cnt += 1

for i in range(7):
    for j in range(2, 5):
        if li[j-2][i] == li[j+2][i] and li[j-1][i] == li[j+1][i]:
            cnt += 1

print(cnt)