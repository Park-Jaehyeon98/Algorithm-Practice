# -*- coding: utf-8 -*-
"""38.K번째 수

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bGjAaZ1NnP9FKBN4HitXNd5FvsVA5zRi
"""

def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        array1 = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(array1[commands[i][2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))