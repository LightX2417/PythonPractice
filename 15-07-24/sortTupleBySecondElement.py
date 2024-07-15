# Write a program to sort a tuple of tuples by 2nd item.

t1 = (("c", 3), ("z", 26), ("a", 1), ("j", 10))
sec = [x[1] for x in t1]
res = ()
sec.sort()
for x in sec:
    for y in t1:
        if y[1] == x:
            res += (y,)
print(res)
