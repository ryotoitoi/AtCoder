import io
import sys

_INPUT = """\
100 4 16
"""
sys.stdin = io.StringIO(_INPUT)

n,a,b=map(int,input().split())
import copy
sum=0
for i in range(n+1):
  ans=0
  x=copy.copy(i)
  while i>0:
        ans+=i%10
        i=i//10
  if a<= ans <=b:
        sum+=x

print(sum)   



