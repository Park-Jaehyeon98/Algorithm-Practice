# -*- coding: utf-8 -*-
"""9.정수 내림차순으로 배치하기의 사본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dO5DZzYCyRT4jGzbv5gyjS2JiyqtiBjk
"""

def solution(n):
    answer = True
    a = list(str(n))
    
    hap = sum([int(i) for i in a])

    if n % hap != 0:
        answer = False

    return answer

print(solution(11))