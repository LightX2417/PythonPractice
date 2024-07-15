# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.

t1 = ((1, 2, 12), (2, 3, 4), (3, 4, 7))
t2 = ()
for x in t1:
    res = 0
    for y in x:
        res += y
    t2 += (res,)
print(t2)
