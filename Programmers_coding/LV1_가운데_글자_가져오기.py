# -*- coding: utf-8 -*-
"""21.가운데 글자 가져오기

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ld2o0XMVAPR_mJQXUPE8FKcjWbrUrjv3
"""

def solution(s):
    answer = ''

    if len(s) % 2 == 0:
        answer += s[len(s)//2-1:len(s)//2+1]
    else:
        answer += s[len(s)//2]
    return answer

print(solution("abcde"))
print(solution("qwer"))