# -*- coding: utf-8 -*-
"""48.LV2_JadenCase 문자열 만들기

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X-nPa1R3d9k09SVxHiLaW_0soI3fTIo2
"""

def solution(s):
    answer = ''
    if s[0].islower():
        answer += s[0].upper()
    else:
        answer += s[0]

    for i in range(1, len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i-1] == ' ':
            if s[i].islower():
                answer += s[i].upper()
            else:
                answer += s[i]
        else:
            if s[i].isupper():
                answer += s[i].lower()
            else:
                answer += s[i]
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution("for the 3laSt 6wEek"))