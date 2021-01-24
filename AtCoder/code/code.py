import io
import sys

_INPUT = """\
5 13 7
R B R R B
B R B R R
"""
sys.stdin = io.StringIO(_INPUT)

n,x,y=map(int,input().split())
a=list(input().split())
b=list(input().split())            

sum=0

for i in range(n-1):
      if a[i] != b[i]:
            if a[i]==b[i+1] and a[i+1]==b[i]:
                  if x < y*2:
                        a[i+1] = a[i]
                        sum+=x
                  else:
                        sum+=y
            else:
                  sum+=y

if a[-1]!=b[-1]:
      sum+=y
print(sum)

