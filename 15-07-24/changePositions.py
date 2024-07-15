# Write a Python program to change the position of every n-th value with the (n+1)th in a list

l1 = eval(input("Enter a list"))
for x in range(1, len(l1), 2):
    temp = l1[x]
    l1[x] = l1[x - 1]
    l1[x - 1] = temp
print(l1)
