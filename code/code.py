import io
import sys

_INPUT = """\
5 4 2
2 1 1
3 3 4


"""
sys.stdin = io.StringIO(_INPUT)

W,H,N = map(int,input().split())
a = [input().split() for l in range(N)]
 
X = Y = 0
 
for i in range(N):
  if a[i][2] == "1":
    X = max(X,int(a[i][0]))
    
  elif a[i][2] == "2":
    W = min(W,int(a[i][0]))
    
  elif a[i][2] == "3":
    Y = max(Y,int(a[i][1]))
    
  elif a[i][2] == "4":
    H = min(H,int(a[i][1]))

print(max((W - X),0) * max((H - Y),0))
