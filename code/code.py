import io
import sys

_INPUT = """\
999
1500
"""
sys.stdin = io.StringIO(_INPUT)

x =input()
m = int(input())

x =list(x)
x_sort = sorted(x)
d = x_sort[-1]
d = int(d)
ans = 0

re_x = reversed(x)

for i in range(d+1,d+9**60):
      # print(i)
      cnt = 0
      sum = 0
      for j in re_x:
            sum += int(j)* (i**cnt)
            cnt +=1
      if sum<=m:
            ans +=1
      if sum > m:
            break
      # print(sum)

print(ans)     