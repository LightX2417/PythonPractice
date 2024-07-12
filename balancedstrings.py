# Write a program to check if two strings are 
# balanced. For example, strings s1 and s2 
# are balanced if all the characters in the s1 
# are present in s2. The character’s position 
# doesn’t matter.

s1=input("Enter string 1: ")
s2=input("Enter string 2: ")
if set(s1)==set(s2):
    print("Both the strings are balanced.")
else:
    print("The strings are not balanced.")