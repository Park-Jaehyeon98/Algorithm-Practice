# -*- coding: utf-8 -*-
"""15_수들의 합v2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O7llsY8dW_3DjjhiKv9x0M_SWB22hahv
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
sum = a[0]
cnt = 0
while True:
    if sum < m:
        if rt < n:
            sum += a[rt]
            rt += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= a[lt]
        lt += 1
    else:
        sum -=a [lt]
        lt += 1
print(cnt)