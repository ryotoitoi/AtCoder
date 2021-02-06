import io
import sys

_INPUT = """\
4 4
1 2
1 3
2 4
3 4
3
1 2
1 3
2 3
"""
sys.stdin = io.StringIO(_INPUT)

import itertools

n,m=map(int,input().split())
cond = [tuple(map(int,input().split())) for i in range(m)]
k=int(input())
choice = [tuple(map(int,input().split())) for i in range(k)]
ans=0

for balls in itertools.product(*choice):
    balls=set(balls)
    cnt = sum(A in balls and B in balls for A,B in cond)
    if ans < cnt:
        ans = cnt
print(ans)