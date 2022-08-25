# -*- coding: utf-8 -*-
"""25_마구간 정하기(결정알고리즘)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lr_z6DALTmP9vX5u1fasp42LEzGs50r_
"""

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)

Line.sort()
lt=1
rt=Line[n-1]

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)