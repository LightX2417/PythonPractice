# Write a Python program to print the numbers of a specified list after removing even numbers from it.

l1 = eval(input("Enter a list: "))
l1 = [ x for x in l1 if x%2 !=0]
print(l1)
