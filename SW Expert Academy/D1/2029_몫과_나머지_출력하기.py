# -*- coding: utf-8 -*-
"""2029.몫과 나머지 출력하기

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H4o0iE3QoQ1odepxmalPWdf2_DaQcKes
"""

n = int(input())

for i in range(1, n+1):
    a ,b = map(int, input().split())
    print("#" + str(i) + " " + str(a//b) + " " + str(a%b))