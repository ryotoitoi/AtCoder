import io
import sys

_INPUT = """\
10 3 5 20

"""
sys.stdin = io.StringIO(_INPUT)

n,x = map(int,input().split())
a=list(map(int,input().split()))