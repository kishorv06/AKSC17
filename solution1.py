#!/bin/python3

import math

def display(li):
    for i in range(len(li[0])):
        for j in range(len(li)):
            if(i>=len(li[j])):
                continue
            print(li[j][i], end='')
        print('',end=' ')

s = input().strip(' ')
l=len(s)**0.5
l1=[]
n=0
m=math.ceil(l)
if(l>=(math.floor(l)+0.5)):
    n=math.ceil(l)
else:
    n=math.floor(l)
for i in range(n):
    l1.append(list(s)[i*m:(i+1)*m])
display(l1)
