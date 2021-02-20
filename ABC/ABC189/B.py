import io
import sys

_INPUT = """\
5 5
3 5 6 5 4
"""
sys.stdin = io.StringIO(_INPUT)

n,x = map(int,input().split())
a=list(map(int,input().split()))

l=[]

for i in a:
    if i!=x:
        l.append(i)

if len(l)>0:
    for i in l:
        print(i,end=' ')
else:
    print()
