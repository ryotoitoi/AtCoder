import io
import sys

_INPUT = """\
15 1 3 15 13
...#.#...#.#...
"""
sys.stdin = io.StringIO(_INPUT)

n,a,b,c,d = map(int,input().split())
a,b,c,d=a-1,b-1,c-1,d-1
s=input()
s=[i for i in s]

s[a] = "A"
s[b] = "B"


if c<d:
    for i in range(n):
        if s[d] == "B":
            break
        else:
            if b+2<=len(s)-1 and s[b+2] != "#":
                s[b+2] = "B"
                s[b] = "."
                b=b+2
            elif s[b+1] != "#":
                s[b+1] = "B"
                s[b] = "."
                b=b+1
        
    for i in range(n):
        if s[c] == "A":
            break
        else:
            if a+2<=len(s)-1 and s[a+2] != "#" and s[a+2] != "B":
                s[a+2] = "A"
                s[a] = "."
                a=a+2
            elif s[a+1] != "#" and s[a+1] != "B":
                s[a+1] = "A"
                s[a] = "."
                a=a+1
else:
    for i in range(n):
        if s[c] == "A":
            break
        else:
            if a+2<=len(s)-1 and s[a+2] != "#":
                s[a+2] = "A"
                s[a] = "."
                a=a+2
            elif s[a+1] != "#":
                s[a+1] = "A"
                s[a] = "."
                a=a+1
        
    for i in range(n):
        if s[d] == "B":
            break
        else:
            if b+2<=len(s)-1 and s[b+2] != "#" and s[b+2] != "A":
                s[b+2] = "B"
                s[b] = "."
                b=b+2
            elif s[b+1] != "#" and s[b+1] != "A":
                s[b+1] = "B"
                s[b] = "."
                b=b+1
    

print(s)

if s[c]=="A" and s[d] == "B":
    print("Yes")
else:
    print("No")
