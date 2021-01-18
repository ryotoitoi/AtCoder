num = int(input())
cnt = 0
while num % 2 == 0:
    num //= 2
    cnt += 1
print(cnt)