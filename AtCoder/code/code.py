import io
import sys

_INPUT = """\
15 1 3 15 13
...#.#...#.#...
"""
sys.stdin = io.StringIO(_INPUT)

import sys
input = sys.stdin.readline

N, A, B, C, D = map(int, input().split())
S = input().rstrip()

ans = "No"
if D > C:
    if "##" not in S[A:D]:
        ans = "Yes"
else:
    for i in range(B-1, D):
        if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
            ans = "Yes"
print(ans)

