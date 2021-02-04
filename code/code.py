import io
import sys

_INPUT = """\
15 9
dnsusrayukuaiia
dujrunuma
"""
sys.stdin = io.StringIO(_INPUT)

from math import gcd
N, M = map(int, input().split())
S = input()
T = input()
 
g = gcd(N, M)
l = N * M // g
n=N // g
m=M // g

for i in range(g):
    if S[i * n] != T[i * m]:
        print(-1)
        exit()
else:
    print(l)