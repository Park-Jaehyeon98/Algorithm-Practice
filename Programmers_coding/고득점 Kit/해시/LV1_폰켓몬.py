# -*- coding: utf-8 -*-
"""LV1.폰켓몬

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Owl9-jHdzyq0EJFbAlQB8cYLqdlgsKN
"""

def solution(nums):
    answer = 0
    cnt = len(nums)//2
    nums = list(set(nums))
    if len(nums) >= cnt:
        answer = cnt
    else:
        answer = len(nums)
    return answer

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))