import io
import sys

_INPUT = """\
6
3 1 2 4 2 1
"""
sys.stdin = io.StringIO(_INPUT)

n=int(input())
a=list(map(int,input().split()))
from collections import Counter
a_counter = Counter(a)

print(a_counter)






      