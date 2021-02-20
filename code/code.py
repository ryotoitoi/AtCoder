import io
import sys

_INPUT = """\
6174 100000

"""
sys.stdin = io.StringIO(_INPUT)

n,k = list(map(int,input().split()))

for i in range(k):
  n = str(n)
  n = list(n)
  # print(n)
  n = sorted(n)
  nn = reversed(n)
  # print(nn)
  g_1 = ''.join(nn)
  g_2 = ''.join(n)
  # print(g_1)
  # print(g_2)
  if '0' in str(g_2):
    g_2 = g_2.replace('0','')
  fx = int(g_1) - int(g_2)
  if fx ==0:
        n = fx
        break
  n = fx
  # print(fx)

print(n)