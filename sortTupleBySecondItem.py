# Write a program to sort a tuple of tuples by 2nd item.
# Sample:
# ((‘r’,3),(‘t’,1),(‘e’,2),(‘y’,9))
# Expected Output: 
# ((‘t’,1),(‘e’,2),(‘r’,3),(‘y’,9))


t1=eval(input("Enter a tuple: "))
sec=[x[1] for x in t1]
res=()
sec.sort()
for x in sec:
    for y in t1:
        if y[1]==x:
            res+=(y,)
print(res)