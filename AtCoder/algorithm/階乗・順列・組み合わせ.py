# 階乗
import math
math.factorial(n)

# 組み合わせの総数を返す関数
import math
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

# 順列の総数を返す関数
from scipy.special import perm

print(perm(4, 2))
# 12.0

print(perm(4, 2, exact=True))
# 12

print(perm(4, 4, exact=True))
# 24