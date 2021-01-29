import io
import sys

_INPUT = """\
a
6
2 2 a
2 1 b
1
2 2 c
1
1

"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque
s=deque(input())
q=int(input())
l=[list(map(str,input().split())) for i in range(q)]

cnt=0

for i in l:
    if i[0]=='1':
        cnt+=1
    else:
        if cnt%2==0:
            if i[1]=='1':
                s.appendleft(i[2])
            else:
                s.append(i[2])
        else:
            if i[1]=='1':
                s.append(i[2])
            else:
                s.appendleft(i[2])

if cnt%2==1:
    s.reverse()
ans=''.join(s)
print(ans)