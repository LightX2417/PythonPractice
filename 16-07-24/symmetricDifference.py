s1 = int(input())
arr1 = set(list(map(int, input().split())))
s2 = int(input())
arr2 = set(list(map(int, input().split())))
diff = sorted(list(arr1.symmetric_difference(arr2)))
for item in diff:
    print(item)
