import io
import sys

_INPUT = """\


"""
sys.stdin = io.StringIO(_INPUT)

h,w=map(int,input().split())

s=[list(map(str,input().split())) for i in range(h)]

