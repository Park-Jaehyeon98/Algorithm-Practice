# -*- coding: utf-8 -*-
"""29.최대공약수와 최소공배수

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LJ1ipXTnc9PJUCwzNaLKXYTv_ynNp6dG
"""

def solution(n, m):
    answer = []

    for i in range(min(n,m), 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
        
    for i in range(max(n,m), n*m+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break

    return answer

print(solution(3, 12))
print(solution(2, 5))