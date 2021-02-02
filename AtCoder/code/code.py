import io
import sys

_INPUT = """\
4 4
1 2
1 3
2 4
3 4
4
3 4
1 2
2 4
2 4


"""
sys.stdin = io.StringIO(_INPUT)

n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
k=int(input())
cd=[list(map(int,input().split())) for i in range(k)]

lst=[]
for i in cd:
    if i[0] not in lst:
        lst.append(i[0])
    else:
        lst.append(i[1])

lst_1=[]
for i in cd:
    if i[1] not in lst_1:
        lst_1.append(i[1])
    else:
        lst_1.append(i[0])

cnt=0
for i in ab:
    if i[0] in lst and i[1] in lst:
        cnt+=1
cnt1=0
for i in ab:
    if i[0] in lst_1 and i[1] in lst_1:
        cnt1+=1

print(max(cnt,cnt1))