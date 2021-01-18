import io
import sys

_INPUT = """\
2 2 1 1
"""
sys.stdin = io.StringIO(_INPUT)

n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
l_a=[]
l_b=[]

for i in range(n):
      if i %2==0:
            l_a.append(a[i])
      else:
            l_b.append(a[i])
ans=sum(l_a)-sum(l_b)
print(ans)
      
      






      