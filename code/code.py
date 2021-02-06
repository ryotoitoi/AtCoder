import io
import sys

_INPUT = """\
7
3 1
4 1
5 9
2 6
5 3
5 8
9 7

"""
sys.stdin = io.StringIO(_INPUT)

N=int(input())
S=0
L=[]
for i in range(0,N):
  A,B=map(int,input().split())
  L+=[[A,B]]
for X in reversed(L):
  A=X[0]
  B=X[1]
  if (A+S)%B!=0:
    S+=((A+S)//B+1)*B-A-S
print(S)