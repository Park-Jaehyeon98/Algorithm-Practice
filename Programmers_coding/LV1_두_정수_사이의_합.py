# -*- coding: utf-8 -*-
"""14.두 정수 사이의 합

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-XSs5qDjv1qBTHw5Y7eVSOS1EZFlJaT8
"""

def solution(a, b):
    answer = 0
    for i in range(max(a,b) - min(a,b) + 1):
        answer += max(a,b) - i

    return answer

print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))