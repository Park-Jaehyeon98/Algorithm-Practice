# -*- coding: utf-8 -*-
"""bj1920.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LderkQwFzHh4FqLoNgz6O-K40hAPo39s
"""

# 1920번 : 수찾기

def find_number(total_list, find_num):
    start = 0
    mid = len(total_list) // 2
    end = len(total_list) - 1

    while start <= end:
        if total_list[mid] == find_num:
            return 1
        elif total_list[mid] > find_num:
            end = mid - 1
        else:
            start = mid + 1

        mid = start + (end - start) // 2
    
    return 0

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(m):
    print(find_number(a, b[i]))