# Write a program to swap two tuples.

t1 = (1, 2, 3, 4)
t2 = (10, 20, 30, 40)
print(t1, t2)
temp = t2
t2 = t1
t1 = temp
print(t1, t2)
