# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true

from collections import Counter

n = int(input())
l1 = [input().strip() for i in range(n)]
res = Counter(l1)
print(len(res))
print(*res.values())
