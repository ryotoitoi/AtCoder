# 浮動小数点の扱いに注意

import io
import sys

_INPUT = """\
42782.4720 31949.0192 99999.99

"""
sys.stdin = io.StringIO(_INPUT)

import math
from decimal import Decimal

x,y,r=input().split()
x,y,r=Decimal(x),Decimal(y),Decimal(r)

low=math.ceil(x-r)
high = math.floor(x+r)

ans=0

for i in range(low,high+1):
    p = pow(r,2)-pow(x-i,2)
    p=p.sqrt()
    # p=math.sqrt(r**2 - (x-i)**2)
    top= math.floor(y+p)
    bottom= math.ceil(y-p)
    ans += (top-bottom)+1

print(ans)
