# -*- coding: utf-8 -*-
"""36.최소직사각형

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11_UeUk5pqYtco5j1Hyq9q8vrP-Zcg1wm
"""

def solution(sizes):
    maxx = []
    minn = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            maxx.append(sizes[i][0])
            minn.append(sizes[i][1])
        else:
            maxx.append(sizes[i][1])
            minn.append(sizes[i][0])
            
    return max(maxx)*max(minn)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))