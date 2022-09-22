# -*- coding: utf-8 -*-
"""31.같은 숫자는 싫어

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y-jvBRwYvSvQcsT0HRITzcx-ublDx-lv
"""

def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))