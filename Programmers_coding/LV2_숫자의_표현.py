# -*- coding: utf-8 -*-
"""52.LV2 숫자의 표현

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9sc4_1ZriMT_wVpr-h0X2i2NdHwZHes
"""

def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        for j in range(i, n+1):
            cnt += j
            if cnt == n:
                answer += 1
                break
            elif cnt > n:
                break    
    return answer

print(solution(15))