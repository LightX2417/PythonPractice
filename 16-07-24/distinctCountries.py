# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

n = int(input())
distinct_countries = set()
for x in range(n):
    distinct_countries.add(input())
print(len(distinct_countries))
