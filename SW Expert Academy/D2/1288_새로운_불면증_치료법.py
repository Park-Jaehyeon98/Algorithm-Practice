# -*- coding: utf-8 -*-
"""1288.새로운 불면증 치료법

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EA1B9zG80I1sje05Oii49ayzt95xuBtY
"""

n = int(input())

for i in range(1, n+1):
    a = int(input())
    b = []
    j = 1
    while True:
        num = a*j
        while num > 0:
            b.append(num%10)
            num = num//10
        b = list(set(b))
        if len(b) == 10:
            break
        j += 1
    print(f'#{i} {j*a}')