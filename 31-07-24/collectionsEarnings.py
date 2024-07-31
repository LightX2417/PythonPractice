# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter

x = int(input())
stock = Counter(map(int, input().split()))

earnings = 0

n = int(input())
for i in range(n):
    desiredSize = list(map(int, input().split()))
    if(stock[desiredSize[0]]>0):
        earnings+=desiredSize[1]
        stock[desiredSize[0]]-=1

print(earnings)
    