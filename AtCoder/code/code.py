import io
import sys

_INPUT = """\
5
1 4 3 5 2
"""
sys.stdin = io.StringIO(_INPUT)

n=int(input())
p=list(map(int,input().split()))

l=[]
for i in range(len(p)):
    if p[i] != i+1:
        l.append("○")
    else:
        l.append("×")
print(l)

for i in range(len(l)):
    if i =='○' and i+1 == '×':
        