# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

T = int(input()) #no. of test conditions

for x in range(T):
    nA = int(input())
    A = set(list(map(int, input().split())))
    nB = int(input())
    B = set(list(map(int, input().split())))
    print(A.issubset(B))
