# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

n = input() #used this because the question required two integer inputs in the beginning which were not relevant
arr = list(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1
print(happiness)
