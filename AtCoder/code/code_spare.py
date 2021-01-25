import io
import sys

_INPUT = """\
5
OR
OR
OR
OR
OR
"""
sys.stdin = io.StringIO(_INPUT)

n=int(input())
s=[input() for i in range(n)]

ans=1
cnt=1
lst=[]

for i in s:
      if i =="OR":
            cnt+=1
            t=2*cnt-1
            f=1
      else:
            t=2**cnt-1
            cnt=1
            lst.append(t)
