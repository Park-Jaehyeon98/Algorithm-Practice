# -*- coding: utf-8 -*-
"""LV2.모음사전

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q1Fs18xf06jUz0XOipxvTPJy8KzPMtEl
"""

def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / 4 * "AEIOU".index(n) + 1
    return int(answer)

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))