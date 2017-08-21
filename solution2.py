#!/bin/python
import sys
import math

s = raw_input().strip()
l = len(s)
m = int(math.floor(math.sqrt(l)))
M = int(math.ceil(math.sqrt(l)))
a = sys.maxint
r = c = 0
for i in range(m,M+1):
    for j in range(i,M+1):
        if(i*j>=l and i*j<a):
            a = i*j
            r = i
            c = j
op = []
for i in range(c):
    row = ""
    for j in range(r):
        if(j*c+i < l):
            row += s[j*c+i]
    op.append(row)
print " ".join(op)
