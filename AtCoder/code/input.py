n=1

# 複数・整数
map(int,input().split())

# リスト1行
list(map(int,input().split()))

# リスト複数行・複数列
[list(map(int,input().split())) for i in range(n)]
[list(map(str,input().split())) for i in range(n)]

# 複数行・1列
[int(input()) for i in range(n)]


