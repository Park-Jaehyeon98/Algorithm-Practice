# -*- coding: utf-8 -*-
"""4676.늘어지는 소리 만들기

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lalmaCfImiAQF_VaS-5FXb-WN8AzLs9z
"""

t = int(input())

for i in range(1, t+1):
    word = list(map(str, input()))
    num = int(input())
    idx = list(map(int, input().split()))
    idx.sort(reverse = True)

    for j in idx:
        word.insert(j, '-')
    word = ''.join(word)
    print(f'#{i} {word}')