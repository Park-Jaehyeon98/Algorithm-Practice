# -*- coding: utf-8 -*-
"""2068.최대수 구하기

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vl4xRJkPIeFDrKzleKceLm-_RviR80JI
"""

n = int(input())
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

for i in range(1, n+1):
    print("#" + str(i) +" " + str(max(a[i-1])))