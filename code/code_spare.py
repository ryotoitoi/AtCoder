import io
import sys

_INPUT = """\
963761198400
"""
sys.stdin = io.StringIO(_INPUT)

n=int(input())
cnt=0
for i in range(n+1):
      for j in range(n+1):
            if (1/2)*(j-i+1)*(i+j)==n:
                  cnt+=1
1

